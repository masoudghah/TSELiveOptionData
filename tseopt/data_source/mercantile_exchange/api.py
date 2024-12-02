import time

import requests

from tseopt.data_source.mercantile_exchange import schema
from tseopt.data_source.mercantile_exchange.descriptor import Token


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


class MercantileData:
    def __init__(self, mercantile_exchange: MercantileExchange) -> None:
        self._api = mercantile_exchange
        self._data: list[schema.Markets] = []

    def update_data(self, timeout: int = 20) -> None:
        self._data = self._api.get_data(timeout=timeout)

    def _get_specific_market(self, market_name: schema.MarketNames) -> schema.GeneralDataType:
        if self._data == []:
            raise ValueError("There is no data. Please ensure that you have updated the data using the update_data method.")
        for record in self._data:
            if record["M"] == market_name:
                return record["A"][0]
        else:
            raise ValueError("Invalid market_name")

    @property
    def gavahi(self) -> list[schema.Type1Data]:
        return self._get_specific_market("updateGavahiMarketsInfo")

    @property
    def sandoq(self) -> list[schema.Type1Data]:
        return self._get_specific_market("updateSandoqMarketsInfo")

    @property
    def salaf(self) -> list[schema.Type1Data]:
        return self._get_specific_market("updateSalafMarketsInfo")

    @property
    def cdc(self) -> list[schema.CDCData]:
        return self._get_specific_market("updateCDCMarketsInfo")

    @property
    def all_market(self) -> schema.AllMarketData:
        return self._get_specific_market("updateAllMarketData")

    @property
    def future_date_time(self) -> None:
        return self._get_specific_market("updateFutureDateTime")

    @property
    def future(self) -> list[schema.FutureData]:
        return self._get_specific_market("updateFutureMarketsInfo")

    @property
    def markets_info(self) -> list[schema.UpdateMarketInfo]:
        return self._get_specific_market("updateMarketsInfo")


def make_a_mercantile_data_object() -> MercantileData:
    me = MercantileExchange(mercantile_exchange_api=_mercantile_exchange_api)
    return MercantileData(me)


if __name__ == "__main__":
    md = make_a_mercantile_data_object()
    md.update_data()
    print(md.gavahi[0])
    print(md.sandoq[0])
    print(md.salaf[0])
    print(md.cdc[0])
    print(md.all_market)
    print(md.future_date_time)
    print(md.future[0])
    print(md.markets_info[0])


