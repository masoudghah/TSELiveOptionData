from concurrent.futures import ThreadPoolExecutor
from typing import Literal

import pandas as pd
import requests
from fake_useragent import UserAgent

from data_source.tsetmc import schema

fake_user_agent = UserAgent()


def fetch_option_data(market: Literal["bourse", "fara_bourse"]) -> list[schema.OptionData]:
    market_num = schema.MARKETS_NUM.get(market)

    if market_num is None:
        raise ValueError("Invalid market value. Expected 'bourse' or 'fara_bourse'.")

    url = f"https://cdn.tsetmc.com/api/Instrument/GetInstrumentOptionMarketWatch/{market_num}"
    headers = {'User-Agent': fake_user_agent.random}
    try:
        response = requests.get(url=url, headers=headers)
        response.raise_for_status()
        json_response: schema.OptionDataOutput = response.json()
        return json_response.get("instrumentOptMarketWatch")
    except requests.RequestException as e:
        print(f"An error occurred while fetching option data: {e}")
        raise


def fetch_entire_market_data() -> list[schema.OptionData]:
    with ThreadPoolExecutor(max_workers=2) as executor:
        bourse_future = executor.submit(fetch_option_data, market="bourse")
        fara_bourse_future = executor.submit(fetch_option_data, market="fara_bourse")
    return bourse_future.result() + fara_bourse_future.result()


def clean_entire_market_data(raw_data: list[schema.OptionData]) -> pd.DataFrame:
    df = pd.DataFrame(raw_data)

    general_columns = [column for column in df.columns if (not column.endswith("_P")) and (not column.endswith("_C"))]
    specific_columns = [column.replace("_C", "") for column in df.columns if column.endswith("_C")]

    calls = df[general_columns + [column + "_C" for column in specific_columns]]
    calls.columns = [column.replace("_C", "") for column in calls.columns]
    calls = calls.rename(columns=schema.SPECIFIC_COLUMN_NAMES)
    calls['option_type'] = 'call'

    puts = df[general_columns + [column + "_P" for column in specific_columns]]
    puts.columns = [column.replace("_P", "") for column in puts.columns]
    puts = puts.rename(columns=schema.SPECIFIC_COLUMN_NAMES)
    puts['option_type'] = 'put'

    # Concatenate the calls and puts DataFrames
    result_df = pd.concat([calls, puts], ignore_index=True)
    result_df.rename(columns=schema.GENERAL_COLUMN_NAMES, inplace=True)
    return result_df


def fetch_cleaned_entire_market_data() -> pd.DataFrame:
    """
    Fetch and clean the entire option market data.

    Returns:
        pd.DataFrame: A DataFrame containing the following columns:
            - 'contract_size': Size of the contract.
            - 'ua_tse_code': Unique identifier for the underlying asset.
            - 'ua_ticker': Ticker symbol for the underlying asset used in the market.
            - 'ua_close_price': Closing price of the underlying asset.
            - 'ua_yesterday_price': Closing price of the underlying asset from the previous day.
            - 'begin_date': Start date of the option contract.
            - 'end_date': Expiration date of the option contract.
            - 'strike_price': Strike price for the option.
            - 'days_to_maturity': Number of days remaining until expiration.
            - 'tse_code': Unique identifier for the option.
            - 'last_price': Last traded price of the option.
            - 'open_positions': Number of open positions for the option.
            - 'close_price': Closing price of the option.
            - 'yesterday_price': Price of the option from the previous trading session.
            - 'notional_value': Total monetary value of the option contract.
            - 'trades_value': Total value of trades executed for the option.
            - 'trades_volume': Volume of trades executed for the option.
            - 'trades_num': Number of trades executed for the option.
            - 'name': Name of the financial instrument (e.g., 'اختيارخ اهرم-26000-1403/08/30').
            - 'ticker': Ticker symbol for the option used in the market.
            - 'bid_price': Highest price a buyer is willing to pay for the option.
            - 'bid_volume': Volume of the option available at the bid price.
            - 'ask_price': Lowest price a seller is willing to accept for the option.
            - 'ask_volume': Volume of the option available at the ask price.
            - 'yesterday_open_positions': Number of open positions from the previous day.
            - 'option_type': Type of the option (e.g., call or put).
    """
    raw_data = fetch_entire_market_data()
    return clean_entire_market_data(raw_data)


if __name__ == "__main__":
    from pprint import pprint
    data = fetch_cleaned_entire_market_data()
    data.to_csv(path_or_buf="TSETMC_sample_data.csv", index=False)
    pprint(data.to_dict("records")[0])



