from typing import TypedDict


class OptionData(TypedDict):
    insCode_P: str
    insCode_C: str
    contractSize: int
    uaInsCode: str
    lVal18AFC_P: str
    lVal30_P: str
    zTotTran_P: int
    qTotTran5J_P: int
    qTotCap_P: float
    notionalValue_P: float
    pClosing_P: int
    priceYesterday_P: int
    oP_P: int
    pDrCotVal_P: int
    lval30_UA: str
    pClosing_UA: int
    priceYesterday_UA: int
    beginDate: str
    endDate: str
    strikePrice: int
    remainedDay: int
    pDrCotVal_C: int
    oP_C: int
    pClosing_C: int
    priceYesterday_C: int
    notionalValue_C: float
    qTotCap_C: float
    qTotTran5J_C: int
    zTotTran_C: int
    lVal30_C: str
    lVal18AFC_C: str
    pMeDem_P: int
    qTitMeDem_P: int
    pMeOf_P: int
    qTitMeOf_P: int
    pMeDem_C: int
    qTitMeDem_C: int
    pMeOf_C: int
    qTitMeOf_C: int
    yesterdayOP_C: int
    yesterdayOP_P: int


class OptionDataOutput(TypedDict):
    instrumentOptMarketWatch: list[OptionData]


MARKETS_NUM: dict[str, int] = {
    "bourse": 1,
    "fara_bourse": 2
}

GENERAL_COLUMN_NAMES: dict[str, str] = {
    "uaInsCode": "ua_tse_code",
    "lval30_UA": "ua_ticker",
    "remainedDay": "days_to_maturity",
    "strikePrice": "strike_price",
    "contractSize": "contract_size",
    "pClosing_UA": "ua_close_price",
    "priceYesterday_UA": "ua_yesterday_price",
    "beginDate": "begin_date",
    "endDate": "end_date",
}

SPECIFIC_COLUMN_NAMES: dict[str, str] = {
    'insCode': "tse_code",
    'lVal18AFC': "ticker",
    'zTotTran': "trades_num",
    'qTotTran5J': "trades_volume",
    'qTotCap': "trades_value",
    'pDrCotVal': "last_price",
    'pClosing': "close_price",
    'priceYesterday': "yesterday_price",
    'oP': "open_positions",
    'yesterdayOP': "yesterday_open_positions",
    'notionalValue': "notional_value",
    'pMeDem': "bid_price",
    'qTitMeDem': "bid_volume",
    'pMeOf': "ask_price",
    'qTitMeOf': "ask_volume",
    'lVal30': "name",
}
