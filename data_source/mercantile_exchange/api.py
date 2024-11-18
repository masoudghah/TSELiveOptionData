import time

import requests

from data_source.mercantile_exchange import schema
from data_source.mercantile_exchange.descriptor import Token


class MercantileExchangeAPI:

    _BASE_URL: str = "https://cdn.ime.co.ir/realTimeServer/"

    @property
    def _timestamp(self) -> str:
        return str(time.time()).replace(".", "")[:13]

    @property
    def _general_params(self) -> dict:
        return {'clientProtocol': "2.1", 'connectionData': '[{"name":"marketshub"}]'}

    def _send_request(self, action: str, method: str, **kwargs) -> schema.APIResponse:
        url = self._BASE_URL + action
        response = requests.request(method=method, url=url, **kwargs)
        response.raise_for_status()
        return response.json()

    def send_negotiate_request(self) -> schema.NegotiateResponse:
        action = "negotiate"
        params = self._general_params | {'_': self._timestamp}
        return self._send_request(action=action, method="get", params=params)

    def send_connect_request(self, connection_token: str) -> schema.ConnectResponse:
        action = "connect"
        params = self._general_params | {'transport': 'longPolling', 'connectionToken': connection_token}
        return self._send_request(action=action, method="post", params=params)

    def send_start_request(self, connection_token: str) -> schema.StartResponse:
        action = "start"

        params = self._general_params | {
            'transport': 'longPolling',
            'connectionToken': connection_token,
            '_': self._timestamp
        }
        return self._send_request(action=action, method="post", params=params)

    def send_poll_request(self, connection_token: str, message_id: str, timeout: int) -> schema.PollResponse:
        action = "poll"
        params = self._general_params | {'transport': 'longPolling', 'connectionToken': connection_token}
        data = f'messageId={message_id}'
        return self._send_request(action=action, method="post", params=params, data=data, timeout=timeout)


_mercantile_exchange_api = MercantileExchangeAPI()


class MercantileExchange:

    message_id = Token()
    connection_token = Token()

    def __init__(self, mercantile_exchange_api: MercantileExchangeAPI) -> None:
        self._api = mercantile_exchange_api

    def _set_connection_token(self) -> None:
        negotiate_response = self._api.send_negotiate_request()
        self.connection_token = negotiate_response.get("ConnectionToken")

    def _set_first_message_id(self) -> None:
        connect_response = self._api.send_connect_request(connection_token=self.connection_token)
        self.message_id = connect_response.get("C")

    def _initialize_tokens(self) -> None:
        self._set_connection_token()
        self._set_first_message_id()

        res = self._api.send_start_request(connection_token=self.connection_token)
        if res.get("Response") != "started":
            raise ValueError("Failed to start.")

    def get_data(self, timeout: int = 20) -> list[schema.Markets]:
        if (self.connection_token and self.message_id) is None:
            self._initialize_tokens()

        res = self._api.send_poll_request(self.connection_token, message_id=self.message_id, timeout=timeout)
        self.message_id = res.get("C")
        return res.get("M")


def make_a_mercantile_exchange_object() -> MercantileExchange:
    return MercantileExchange(mercantile_exchange_api=_mercantile_exchange_api)
