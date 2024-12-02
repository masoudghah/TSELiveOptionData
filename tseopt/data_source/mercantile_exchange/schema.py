from typing import TypedDict, Literal, TypeAlias


class NegotiateResponse(TypedDict):
    Url: str
    ConnectionToken: str
    ConnectionId: str
    KeepAliveTimeout: float
    DisconnectTimeout: float
    ConnectionTimeout: float
    TryWebSockets: bool
    ProtocolVersion: str
    TransportConnectTimeout: float
    LongPollDelay: float


class ConnectResponse(TypedDict):
    C: str
    S: int
    M: list


class StartResponse(TypedDict):
    Response: str


class Type1Data(TypedDict):
    ID: str
    Code: str
    Symbol: str
    Name: str
    YesterdayPrice: float
    FinalPrice: float
    LastPrice: float
    PriceChange: float
    FirstPrice: float
    MinPrice: float
    MaxPrice: float
    Quantity: int
    Volume: float
    Value: float
    DemandVolume1: int
    DemandQuantity1: int
    DemandPrice1: float
    OfferPrice1: float
    OfferQuantity1: int
    OfferVolume1: int
    DemandVolume2: int
    DemandQuantity2: int
    DemandPrice2: float
    OfferPrice2: float
    OfferQuantity2: int
    OfferVolume2: int
    DemandVolume3: int
    DemandQuantity3: int
    DemandPrice3: float
    OfferPrice3: float
    OfferQuantity3: int
    OfferVolume3: int
    DemandVolume4: int
    DemandQuantity4: int
    DemandPrice4: float
    OfferPrice4: float
    OfferQuantity4: int
    OfferVolume4: int
    DemandVolume5: int
    DemandQuantity5: int
    DemandPrice5: float
    OfferPrice5: float
    OfferQuantity5: int
    OfferVolume5: int
    Time: str
    Status: bool
    Buy_CountI: int
    Buy_CountN: int
    Buy_I_Volume: float
    Buy_N_Volume: float
    Sell_CountI: int
    Sell_CountN: int
    Sell_I_Volume: float
    Sell_N_Volume: float
    ModifyDate: str
    ModifyTime: str


class CDCData(TypedDict):
    ContractID: int
    ContractCode: str
    ContractDescription: str
    LastTradingPersianDate: str
    ContractSize: float
    ContractSizeUnitFaDesc: str
    TotalAssetChangesColor: str
    ContractCurrencyFaDesc: str
    LastSettlementPrice: float
    AskPrice1: float
    AskVolume1: int
    AskPrice2: float
    AskVolume2: int
    AskPrice3: float
    AskVolume3: int
    AskTotalVolume: int
    BidPrice1: float
    BidVolume1: int
    BidPrice2: float
    BidVolume2: int
    BidPrice3: float
    BidVolume3: int
    BidTotalVolume: int
    ContractCurrencyEnDesc: str
    LastSettlementPricePersianDate: str
    LastUpdate: str
    HighTradedPriceChanges: float
    HighTradedPrice: float
    LastTradedPriceChangesColor: str
    LastTradedPriceChangesVisibility: str
    LastTradedPriceChangesPercent: float
    LastTradedPriceChanges: float
    LastTradedPriceTime: str
    LastTradedPrice: float
    FirstTradedPriceChangesColor: str
    FirstTradedPriceChangesVisibility: str
    FirstTradedPriceChangesPercent: float
    FirstTradedPriceChanges: float
    FirstTradedPriceTime: str
    FirstTradedPrice: float
    HighTradedPriceChangesPercent: float
    HighTradedPriceChangesVisibility: str
    HighTradedPriceChangesColor: str
    LowTradedPrice: float
    TotalAssetChangesVisibility: str
    TotalAssetChangesPercent: float
    TotalAssetChanges: float
    TotalAsset: float
    TradesValueCurrencyEnDesc: str
    TradesValueCurrencyFaDesc: str
    OrderTimeVisibility: str
    TradesValue: float
    TradesVolume: float
    TradesCount: int
    LowTradedPriceChangesColor: str
    LowTradedPriceChangesVisibility: str
    LowTradedPriceChangesPercent: float
    LowTradedPriceChanges: float
    TradesVolumeVisibility: str
    OrdersPersianDateTime: str
    OrdersDateTime: str
    OrdersCounter: int
    CommodityID: int
    CommodityName: str
    CommodityColor: str
    CommodityColor1: str
    TradesCounter: int
    IsOrdersHighLight: bool
    IsTradesHighLight: bool


class FutureData(TypedDict):
    ContractID: int
    LastTradingDate: str
    ContractCode: str
    ContractDescription: str
    ContractSize: float
    ContractSizeUnitFaDesc: str
    ContractSizeUnitEnDesc: str
    ContractCurrencyFaDesc: str
    ContractCurrencyEnDesc: str
    ContractCurrencyDecimalPlaces: int | None
    LastSettlementPrice: float
    LastSettlementPriceDate: str
    YesterdayOpenInterests: float | None
    BidTotalVolume: int
    BidVolume1: int
    BidPrice1: float
    BidVolume2: int
    BidPrice2: float
    BidVolume3: int
    BidPrice3: float
    BidVolume4: int
    BidPrice4: float
    BidVolume5: int
    BidPrice5: float
    AskTotalVolume: int
    AskVolume1: int
    AskPrice1: float
    AskVolume2: int
    AskPrice2: float
    AskVolume3: int
    AskPrice3: float
    AskVolume4: int
    AskPrice4: float
    AskVolume5: int
    AskPrice5: float
    OrdersDateTime: str
    FirstTradedPrice: float
    FirstTradedPriceTime: str
    FirstTradedPriceChanges: float
    FirstTradedPriceChangesPercent: float
    LastTradedPrice: float
    LastTradedPriceTime: str
    LastTradedPriceChanges: float
    LastTradedPriceChangesPercent: float
    HighTradedPrice: float
    HighTradedPriceChanges: float
    HighTradedPriceChangesPercent: float
    LowTradedPrice: float
    LowTradedPriceChanges: float
    LowTradedPriceChangesPercent: float
    AverageTradedPrice: float | None
    OpeningPrice: float | None
    ClosingPrice: float | None
    TradesCount: int
    TradesVolume: int
    TradesValue: float
    TradesValueCurrencyFaDesc: str
    TradesValueCurrencyEnDesc: str
    OpenInterests: int
    OpenInterestsChanges: int
    OpenInterestsChangesPercent: float
    InitialMargin: float
    MaintenanceMargin: float
    LastUpdate: str
    Expired: bool
    LegalBuyerCount: int
    LegalSellerCount: int
    NaturalBuyerCount: int
    NaturalSellerCount: int
    TodayLiveSettlement: float
    TradeCount: int
    TradeVolume: int
    PersianOrdersDateTime: str | None
    PersianLastSettlementPriceDate: str | None
    PesrsianLastTradingDate: str | None


class AllMarketData(TypedDict):
    id: int
    Description: str
    TradeCount: int
    Buyers: int
    Sellers: int
    LegalBuyerCount: int
    NaturalBuyerCount: int
    LegalSellerCount: int
    NaturalSellerCount: int


class UpdateMarketInfo(TypedDict):
    _StrikeLevel: int
    _StrikePrice: float
    _LastUpdate: str
    _PutContractVisibility: str
    _ContractCategory: str
    _CommodityGroup: str
    _ContractSubGroup: str
    _CallContractID: int
    _CallContractCode: str
    _CallContractDescription: str
    _CallLastTradingPersianDate: str
    _CallContractSize: float
    _CallContractSizeUnitFaDesc: str
    _CallContractCurrencyFaDesc: str
    _CallContractCurrencyEnDesc: str
    _CallLastSettlementPrice: float
    _CallLastSettlementPricePersianDate: str
    _CallBidTotalVolume: float
    _CallBidVolume1: float
    _CallBidPrice1: float
    _CallBidVolume2: float
    _CallBidPrice2: float
    _CallBidVolume3: float
    _CallBidPrice3: float
    _CallBidVolume4: int
    _CallBidPrice4: float
    _CallBidVolume5: int
    _CallBidPrice5: float
    _CallAskTotalVolume: float
    _CallAskVolume1: float
    _CallAskPrice1: float
    _CallAskVolume2: float
    _CallAskPrice2: float
    _CallAskVolume3: float
    _CallAskPrice3: float
    _CallAskVolume4: int
    _CallAskPrice4: float
    _CallAskVolume5: int
    _CallAskPrice5: float
    _CallOrdersDateTime: str
    _CallOrdersPersianDateTime: str
    _CallOrderTimeVisibility: str
    _CallFirstTradedPrice: float
    _CallFirstTradedPriceTime: str
    _CallFirstTradedPriceChanges: float
    _CallFirstTradedPriceChangesPercent: float
    _CallFirstTradedPriceChangesVisibility: str
    _CallFirstTradedPriceChangesColor: str
    _CallLastTradedPrice: float
    _CallLastTradedPriceTime: str
    _CallLastTradedPriceChanges: float
    _CallLastTradedPriceChangesPercent: float
    _CallLastTradedPriceChangesVisibility: str
    _CallLastTradedPriceChangesColor: str
    _CallHighTradedPrice: float
    _CallHighTradedPriceChanges: float
    _CallHighTradedPriceChangesPercent: float
    _CallHighTradedPriceChangesVisibility: str
    _CallHighTradedPriceChangesColor: str
    _CallInitialMargin: float
    _CallRequiredMargin: float
    _CallLowTradedPrice: float
    _CallLowTradedPriceChanges: float
    _CallLowTradedPriceChangesPercent: float
    _CallLowTradedPriceChangesVisibility: str
    _CallLowTradedPriceChangesColor: str
    _CallTradesCount: int
    _CallTradesVolume: float
    _CallTradesVolumeVisibility: str
    _CallTradesValue: float
    _CallTradesValueCurrencyFaDesc: str
    _CallTradesValueCurrencyEnDesc: str
    _CallOpenInterests: float
    _CallOpenInterestsChanges: float
    _CallOpenInterestsChangesPercent: float
    _CallOpenInterestsChangesVisibility: str
    _CallOpenInterestsChangesColor: str
    _PutContractID: int
    _PutContractCode: str
    _PutContractDescription: str
    _PutLastTradingPersianDate: str
    _PutContractSize: float
    _PutContractSizeUnitFaDesc: str
    _PutContractCurrencyFaDesc: str
    _PutContractCurrencyEnDesc: str
    _PutLastSettlementPrice: float
    _PutLastSettlementPricePersianDate: str
    _PutBidTotalVolume: float
    _PutBidVolume1: float
    _PutBidPrice1: float
    _PutBidVolume2: float
    _PutBidPrice2: float
    _PutBidVolume3: float
    _PutBidPrice3: float
    _PutBidVolume4: int
    _PutBidPrice4: float
    _PutBidVolume5: int
    _PutBidPrice5: float
    _PutAskTotalVolume: float
    _PutAskVolume1: float
    _PutAskPrice1: float
    _PutAskVolume2: float
    _PutAskPrice2: float
    _PutAskVolume3: float
    _PutAskPrice3: float
    _PutAskVolume4: int
    _PutAskPrice4: float
    _PutAskVolume5: int
    _PutAskPrice5: float
    _PutOrdersDateTime: str
    _PutOrdersPersianDateTime: str
    _PutOrderTimeVisibility: str
    _PutFirstTradedPrice: float
    _PutFirstTradedPriceTime: str
    _PutFirstTradedPriceChanges: float
    _PutFirstTradedPriceChangesPercent: float
    _PutFirstTradedPriceChangesVisibility: str
    _PutFirstTradedPriceChangesColor: str
    _PutLastTradedPrice: float
    _PutLastTradedPriceTime: str
    _PutLastTradedPriceChanges: float
    _PutLastTradedPriceChangesPercent: float
    _PutLastTradedPriceChangesVisibility: str
    _PutLastTradedPriceChangesColor: str
    _PutHighTradedPrice: float
    _PutHighTradedPriceChanges: float
    _PutHighTradedPriceChangesPercent: float
    _PutHighTradedPriceChangesVisibility: str
    _PutHighTradedPriceChangesColor: str
    _PutInitialMargin: float
    _PutRequiredMargin: float
    _PutLowTradedPrice: float
    _PutLowTradedPriceChanges: float
    _PutLowTradedPriceChangesPercent: float
    _PutLowTradedPriceChangesVisibility: str
    _PutLowTradedPriceChangesColor: str
    _PutTradesCount: int
    _PutTradesVolume: float
    _PutTradesVolumeVisibility: str
    _PutTradesValue: float
    _PutTradesValueCurrencyFaDesc: str
    _PutTradesValueCurrencyEnDesc: str
    _PutOpenInterests: float
    _PutOpenInterestsChanges: float
    _PutOpenInterestsChangesPercent: float
    _PutOpenInterestsChangesVisibility: str
    _PutOpenInterestsChangesColor: str
    StrikeLevel: int
    StrikePrice: float
    LastUpdate: str
    PutContractVisibility: str
    ContractCategory: str
    CommodityGroup: str
    ContractSubGroup: str
    CallOrdersCounter: int
    CallTradesCounter: int
    CallIsOrdersHighLight: bool
    CallIsTradesHighLight: bool


MarketNames: TypeAlias = Literal[
        "updateGavahiMarketsInfo",
        "updateSandoqMarketsInfo",
        "updateSalafMarketsInfo",
        "updateCDCMarketsInfo",
        "updateAllMarketData",
        "updateFutureDateTime",
        "updateFutureMarketsInfo",
        "updateMarketsInfo",
    ]

GeneralDataType: TypeAlias = list[Type1Data | CDCData | FutureData | UpdateMarketInfo] | None | AllMarketData


class Markets(TypedDict):
    H: Literal["marketsHub"]
    M: MarketNames
    A: list[GeneralDataType]


class PollResponse(TypedDict):
    C: str
    M: list[Markets]


APIResponse = NegotiateResponse | ConnectResponse | StartResponse | PollResponse
