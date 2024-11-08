import pandas as pd
import requests

from data_source.tadbir import schema


class Tadbir:

    def __init__(self) -> None:
        self.__base_url = "https://core.tadbirrlc.com//"

    def _make_bulk_data_url(self, isin_list: list[str]) -> str:
        type_: str = "getstockprice2"
        language: str = "Fa"
        base = self.__base_url + "StockInformationHandler"
        arr = ",".join(isin_list)
        query_params = f"%7B%22Type%22:%22{type_}%22,%22la%22:%22{language}%22,%22arr%22:%22{arr}%22%7D"
        return base + "?" + query_params

    def _make_detail_data_url(self, isin: str) -> str:
        type_: str = "getLightSymbolInfoAndQueue"
        language: str = "Fa"
        base = self.__base_url + "StockFutureInfoHandler"
        query_params = f"%7B%22Type%22:%22{type_}%22,%22la%22:%22{language}%22,%22nscCode%22:%22{isin}%22%7D"
        return base + "?" + query_params

    def _get_last_bulk_data_direct(self, isin_list: list[str]) -> list[schema.BulkDataOutput]:
        url = self._make_bulk_data_url(isin_list)
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"An error occurred while fetching data from Tadbir: {e}")
            raise

    def get_last_bulk_data(self, isin_list: list[str]) -> list[dict]:
        length = len(isin_list)
        if length <= 500:
            return self._get_last_bulk_data_direct(isin_list)

        response = []
        for start in range(0, length, 500):
            end = min(start + 500, length)
            partial_response = self._get_last_bulk_data_direct(isin_list[start: end])
            # print(start, end)
            response.extend(partial_response)
        return response

    def get_detail_data(self, isin: str) -> schema.DetailDataOutput:
        url = self._make_detail_data_url(isin)
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"An error occurred while fetching data from Tadbir: {e}")
            raise


class TadbirCleanedData:

    def __init__(self, tadbir: Tadbir) -> None:
        self.__tadbir = tadbir

    def get_last_bulk_data(self, isin_list: list[str]) -> pd.DataFrame:
        """
        isin_list: List of ISINs, e.g., ["IRO9AHRM6981", "IRO9AHRM6911", "IRO9IKCO81M1"]
        """
        raw_data = self.__tadbir.get_last_bulk_data(isin_list)
        data = pd.DataFrame(raw_data)
        return data.rename(columns=schema.BULK_DATA_COLUMN_NAMES)

    def get_detail_data(self, isin: str) -> dict:
        """
        isin: ISIN code, e.g., "IRO9AHRM6981"
        """
        raw_data = self.__tadbir.get_detail_data(isin)

        output = {
            "symbol_info": {schema.SYMBOL_INFO_COLUMN_NAMES.get(key, key): value for
                            key, value in raw_data["symbolinfo"].items()
                            },
            "order_book": raw_data["symbolqueue"]["Value"]
        }
        return output


tadbir = Tadbir()
tadbir_api = TadbirCleanedData(tadbir)

if __name__ == "__main__":
    from pprint import pprint

    isin_list = ["IRO9AHRM8641", "IRO9AHRM6911", "IRO9IKCO81M1"]

    df = tadbir_api.get_last_bulk_data(isin_list=isin_list)
    data = tadbir_api.get_detail_data(isin_list[0])
    df.to_csv(path_or_buf="Tadbir_sample_data.csv", index=False)

    print(df)
    pprint(data)

