from typing import TypedDict


class RawLOBLevel(TypedDict):
    idn: int
    dEven: int
    hEven: int
    refID: int
    number: int
    qTitMeDem: int
    zOrdMeDem: int
    pMeDem: float
    pMeOf: float
    zOrdMeOf: int
    qTitMeOf: int
    insCode: None


columns_name = dict(
    number="level",
    zOrdMeOf="ask_number",
    qTitMeOf="ask_volume",
    pMeOf="ask_price",
    pMeDem="bid_price",
    qTitMeDem="bid_volume",
    zOrdMeDem="bid_number",
)
