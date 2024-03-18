import pandas as pd


class OptionMarket:

    def __init__(self, last_data: pd.DataFrame) -> None:
        self.data = last_data

    @property
    def total_trade_value(self) -> int:
        total_trade_value = self.data["trades_value"].sum()
        return total_trade_value

    @property
    def extreme_changes_in_open_positions(self) -> dict:
        n: int = 5

        data = self.data.copy()
        data["new_positions"] = data["open_positions"] - data["yesterday_open_positions"]
        best = data.sort_values(by="new_positions", ascending=False).head(n)
        worst = data.sort_values(by="new_positions", ascending=True).head(n)
        output = {
            "best": best[["ticker", "new_positions"]].to_dict("records"),
            "worst": worst[["ticker", "new_positions"]].to_dict("records"),
        }
        return output

    @property
    def most_trade_value(self) -> dict:
        n: int = 5

        data = self.data.sort_values(by="trades_value", ascending=False).copy()
        call = data[["ticker", "trades_value"]][data["option_type"] == "call"].head(n)
        put = data[["ticker", "trades_value"]][data["option_type"] == "put"].head(n)
        return {"call": call.to_dict("records"), "put": put.to_dict("records")}

    @property
    def most_trade_value_by_underlying_asset(self) -> dict:
        g = self.data.groupby(['ua_ticker', 'option_type'])
        data = g.agg({"trades_value": "sum"})
        data = data.pivot_table(index='ua_ticker', columns='option_type', values='trades_value',
                                fill_value=0).reset_index()
        data.columns.name = None
        data["total"] = data["call"] + data["put"]
        return data.sort_values("total", ascending=False).head(5).to_dict("records")


def main():
    from third_parties.tsetmc import get_cleaned_options_data
    from pprint import pprint

    read_data_from_file = False

    if read_data_from_file:
        df = pd.read_csv("data.csv")
    else:
        df = get_cleaned_options_data()
        df.to_csv(path_or_buf="data.csv", index=False)

    option_market = OptionMarket(last_data=df)

    pprint(f"total_trade_value: {option_market.total_trade_value / 1e10:.0f} BT")
    pprint(option_market.most_trade_value)
    pprint(option_market.most_trade_value_by_underlying_asset, sort_dicts=False)
    pprint(option_market.extreme_changes_in_open_positions)


if __name__ == "__main__":
    main()




