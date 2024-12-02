from typing import TypedDict


class BulkDataOutput(TypedDict):
    bbp: float
    bbq: int
    bsp: float
    bsq: int
    bv: float
    cn: str
    cp: float
    cpv: float
    cpvp: float
    cs: int
    csid: None
    ftp: float
    gs: int
    hap: float
    hp: float
    ic: str
    lap: float
    lp: float
    lpv: float
    lpvp: float
    ltp: float
    mnqo: float
    mtd: str
    mxqo: float
    nbb: int
    nbs: int
    nc: str
    nst: int
    nt: int
    pcp: float
    pv: float
    rp: float
    sc: str
    sf: str
    ss: int
    td: str
    tv: float
    vs: str


class SymbolInfoOutput(TypedDict):
    bisin: str
    bltp: float
    bv: int
    cp: float
    cp12: int
    cpv: float
    cpvp: float
    crn: str
    crp: int
    cs: int
    ect: str
    ed: str
    est: str
    gc: str
    gs: int
    hp: int
    ht: float
    ic: str
    im: float
    isFuture: bool
    isagsp: bool
    iscu: bool
    iso: bool
    lot: int
    lp: int
    lpv: float
    lpvp: float
    lt: float
    ltd: str
    ltp: float
    mbop: int
    mcaop: int
    mcop: int
    minprod: int
    mlp: int
    mmop: int
    mp: int
    mt: str
    mxp: int
    nc: str
    nst: int
    nt: int
    op: int
    opts: float
    pcp: float
    pv: float
    rp: float
    sd: str
    sp: float
    st: int
    th: float
    tl: float
    tv: float
    vs: int


class OrderBookLevel(TypedDict):
    BestBuyPrice: float
    BestBuyQuantity: int
    BestSellPrice: float
    BestSellQuantity: int
    NSCCode: str
    NoBestBuy: int
    NoBestSell: int
    Place: int


class SymbolQueueOutput(TypedDict):
    Value: list[OrderBookLevel]


class DetailDataOutput(TypedDict):
    symbolinfo: SymbolInfoOutput
    symbolqueue: SymbolQueueOutput


BULK_DATA_COLUMN_NAMES: dict[str, str] = {
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


SYMBOL_INFO_COLUMN_NAMES: dict[str, str] = {
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