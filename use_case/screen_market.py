import pandas as pd


class OptionMarket:

    def __init__(self, entire_option_market_data: pd.DataFrame) -> None:
        self.__data = entire_option_market_data

    @property
    def total_trade_value(self) -> int:
        return self.__data["trades_value"].sum()

    @property
    def extreme_changes_in_open_positions(self, n: int = 5) -> dict:
        data = self.__data.copy()
        data["new_positions"] = data["open_positions"] - data["yesterday_open_positions"]
        best = data.sort_values(by="new_positions", ascending=False).head(n)
        worst = data.sort_values(by="new_positions", ascending=True).head(n)
        output = {
            "best": best[["ticker", "new_positions"]].to_dict("records"),
            "worst": worst[["ticker", "new_positions"]].to_dict("records"),
        }
        return output

    @property
    def most_trade_value(self, n: int = 5) -> dict:
        data = self.__data.sort_values(by="trades_value", ascending=False).copy()
        call = data[["ticker", "trades_value"]][data["option_type"] == "call"].head(n)
        put = data[["ticker", "trades_value"]][data["option_type"] == "put"].head(n)
        return {"call": call.to_dict("records"), "put": put.to_dict("records")}

    @property
    def most_trade_value_by_underlying_asset(self) -> dict:
        g = self.__data.groupby(['ua_ticker', 'option_type'])
        data = g.agg({"trades_value": "sum"})
        data = data.pivot_table(index='ua_ticker', columns='option_type', values='trades_value',
                                fill_value=0).reset_index()
        data.columns.name = None
        data["total"] = data["call"] + data["put"]
        return data.sort_values("total", ascending=False).head(5).to_dict("records")


if __name__ == "__main__":
    from data_source.tsetmc.api import fetch_cleaned_entire_market_data
    from pprint import pprint

    read_data_from_file = False

    # get market data
    if read_data_from_file:
        entire_option_market_data = pd.read_csv("entire_option_market_data.csv")
    else:
        entire_option_market_data = fetch_cleaned_entire_market_data()
        entire_option_market_data.to_csv(path_or_buf="entire_option_market_data.csv", index=False)

    # screen the market
    option_market = OptionMarket(entire_option_market_data=entire_option_market_data)

    pprint(f"total_trade_value: {option_market.total_trade_value / 1e10:.0f} BT")
    pprint(option_market.extreme_changes_in_open_positions)

    pprint(option_market.most_trade_value)
    pprint(option_market.most_trade_value_by_underlying_asset, sort_dicts=False)
