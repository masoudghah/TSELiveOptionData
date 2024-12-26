from collections.abc import Iterator
from enum import Enum
from functools import cached_property

import pandas as pd


class OptionType(str, Enum):
    CALL = "call"
    PUT = "put"
    BOTH = "both"


class Chains:

    def __init__(self, market_data: pd.DataFrame):
        self._market_data = market_data

    @cached_property
    def underlying_asset_info(self) -> pd.DataFrame:
        ua_info = (
            self._market_data
            .groupby("ua_tse_code")
            .agg({"ua_ticker": "max", "trades_value": "sum"})
            .reset_index()
        )
        ua_info.sort_values(by="trades_value", ascending=False, inplace=True)
        return ua_info[["ua_tse_code", "ua_ticker"]].reset_index(drop=True)

    @cached_property
    def ua_tse_codes(self) -> list[str]:
        return self.underlying_asset_info["ua_tse_code"].tolist()

    def options(self, ua_tse_code: str, option_type: OptionType = OptionType.BOTH) -> pd.DataFrame:
        if ua_tse_code not in self.ua_tse_codes:
            raise ValueError(f"Invalid ua_tse_code: {ua_tse_code}")

        data = self._market_data[self._market_data["ua_tse_code"] == ua_tse_code]

        if option_type != OptionType.BOTH:
            return data[data["option_type"] == option_type]
        return data

    def make_date_chains(
            self,
            ua_tse_code: str,
            option_type: OptionType = OptionType.BOTH
    ) -> Iterator[pd.DataFrame]:
        options = self.options(ua_tse_code, option_type=option_type)
        for date in options["end_date"].sort_values().unique():
            yield options[options["end_date"] == date].sort_values(by="strike_price").reset_index(drop=True)

    def make_strike_price_chains(
            self,
            ua_tse_code: str,
            option_type: OptionType = OptionType.BOTH
    ) -> Iterator[pd.DataFrame]:
        options = self.options(ua_tse_code, option_type=option_type)
        for strike_price in options["strike_price"].sort_values().unique():
            yield options[options["strike_price"] == strike_price].sort_values(by="end_date").reset_index(drop=True)


if __name__ == "__main__":
    from tseopt import get_all_options_data

    market_data = get_all_options_data()
    chains = Chains(market_data)
    ua_tse_code = chains.ua_tse_codes[2]

    date_chain = chains.make_date_chains(ua_tse_code=ua_tse_code, option_type=OptionType.PUT)
    strike_price_chain = chains.make_strike_price_chains(ua_tse_code=ua_tse_code, option_type=OptionType.PUT)

    print(list(date_chain))
