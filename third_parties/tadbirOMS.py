from typing import List

import pandas as pd
import requests

BULK_DATA_COLUMN_NAMES = {
    "bv": "BasisVolume",
    "cp": "ClosingPrice",
    "cn": "CompanyName",
    "bbp": "BestBuyPrice",
    "bbq": "BestBuyQuantity",
    "bsp": "BestSellPrice",
    "bsq": "BestSellQuantity",
    "nbb": "NoBestBuy",
    "nbs": "NoBestSell",
    "ftp": "FirstTradedPrice",
    "gs": "GroupStateID",
    "hap": "HighAllowedPrice",
    "hp": "HighPrice",
    "ltp": "LastTradedPrice",
    "lap": "LowAllowedPrice",
    "lp": "LowPrice",
    "mtd": "MTradeDate",
    "mxqo": "MaxQuantityOrder",
    "mnqo": "MinQuantityOrder",
    "nc": "isin",
    "pcp": "PreClosingPrice",
    "rp": "RefPrice",
    "sc": "SectorCode",
    "sf": "ticker",
    "ss": "SymbolStateId",
    "nst": "TotalNumberOfSharesTraded",
    "nt": "TotalNumberOfTrades",
    "tv": "TotalTradeValue",
    "td": "TradeDate",
    "vs": "varSign",
    "cpv": "ClosingPriceVar",
    "cpvp": "ClosingPriceVarPercent",
    "lpv": "LastTradedPriceVar",
    "lpvp": "LastTradedPriceVarPercent",
    # "th": "TomarrowHigh",
    # "tl": "TomarrowLow",
    "ic": "tse_code",
    "csid": "SectorCodeId",
}


SYMBOL_INFO_COLUMN_NAMES = {
        "est": "Symbol",
        "InsCode": "InsCode",
        "ltp": "LastTradedPrice",
        "bltp": "UA_LastTradedPrice",
        "bisin": "UA_isin",
        "ltd": "TradeDate",
        "cp": "ClosingPrice",
        "lp": "LowPrice",
        "nt": "TotalNumberOfTrades",
        "hp": "HighPrice",
        "nst": "TotalNumberOfSharesTraded",
        "pcp": "YesterdayPrice",
        "minprod": "MinQuantityOrder",
        "mxp": "MaxQuantityOrder",
        "lt": "LowAllowedPrice",
        "ht": "HighAllowedPrice",
        "tv": "TotalTradeValue",
        "rp": "RefPrice",
        "st": "SymbolStateId",
        "ect": "CompanyTitle",
        "gs": "GroupStateID",
        "bv": "BaseVolume",
        "cp12": "CP12",
        "mp": "MaxPercent",
        "mlp": "LowPercent",
        "mt": "MarketType",
        "nc": "NSCCode",
        "iscu": "IsCautionAgreement",
        "isagsp": "IsSepahAgreement",
        "ic": "InstrumentCode",
        "sti": "GroupName",
        "ftp": "FirstTradePrice",
        "fvavg": "Volume90avg",
        "ffp": "FloatPercent",
        "uc": "UnitCount",
        "opts": "TickSize",
        "lot": "LotSize",

        "ed": "exerciseDate",
        "sd": "contractStartDate",
        "im": "initial_margin",
        "op": "openPositionNum",
        "cs": "contractSize",
        "sp": "strikePrice",


}


class TadbirRequestError(Exception):
    pass


class Tadbir:

    def __init__(self) -> None:
        self.__base_url = "https://core.tadbirrlc.com//"

    def _make_bulk_data_url(self, isin_list: List[str]) -> str:
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

    def _get_last_bulk_data_direct(self, isin_list: List[str]) -> List[dict]:
        url = self._make_bulk_data_url(isin_list)
        try:
            response = requests.get(url)
            response.raise_for_status()
            json_response = response.json()
            if not isinstance(json_response, list):
                raise TadbirRequestError("Invalid response format. Expected a list of dictionaries.")
            return json_response
        except (requests.RequestException, ValueError) as e:
            print(f"An error occurred while fetching data from Tadbir: {e}")
            return []

    def get_last_bulk_data(self, isin_list: List[str]) -> List[dict]:
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

    def get_detail_data(self, isin: str) -> dict:
        url = self._make_detail_data_url(isin)
        try:
            response = requests.get(url)
            response.raise_for_status()
            json_response = response.json()
            if not (isinstance(json_response, dict) and {"symbolinfo", "symbolqueue"}.issubset(set(json_response.keys()))):
                raise TadbirRequestError("Invalid response format for detail data.")
            return json_response
        except (requests.RequestException, ValueError) as e:
            print(f"An error occurred while fetching data from Tadbir: {e}")
            return {}


class TadbirCleanedData:

    def __init__(self, tadbir: Tadbir) -> None:
        self.__tadbir = tadbir

    def get_last_bulk_data(self, isin_list: List[str]) -> pd.DataFrame:
        """
        isin_list: List of ISINs, e.g., ["IRO9AHRM6981", "IRO9AHRM6911", "IRO9IKCO81M1"]
        """
        raw_data = self.__tadbir.get_last_bulk_data(isin_list)
        data = pd.DataFrame(raw_data)
        return data.rename(columns=BULK_DATA_COLUMN_NAMES)

    def get_detail_data(self, isin: str) -> dict:
        """
        isin: ISIN code, e.g., "IRO9AHRM6981"
        """
        raw_data = self.__tadbir.get_detail_data(isin)

        output = {
            "symbol_info": {SYMBOL_INFO_COLUMN_NAMES.get(key, key): value for key, value in raw_data["symbolinfo"].items()},
            "order_book": raw_data["symbolqueue"]["Value"]
        }
        return output


tadbir = Tadbir()
tadbir_api = TadbirCleanedData(tadbir)

if __name__ == "__main__":
    from pprint import pprint

    isin_list = ["IRO9AHRM6981", "IRO9AHRM6911", "IRO9IKCO81M1"]

    df = tadbir_api.get_last_bulk_data(isin_list=isin_list)
    data = tadbir_api.get_detail_data(isin_list[0])

    print(df)
    pprint(data)

