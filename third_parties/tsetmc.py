from typing import List, Literal

import pandas as pd
import requests

import asyncio
import aiohttp
import time

general_columns_name = {
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
specific_columns_name = {
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


async def get_option_data(market: Literal["bours", "fara_bours"]) -> List[dict]:
    if market not in ["bours", "fara_bours"]:
        raise ValueError("Invalid market value. Expected 'bours' or 'fara_bours'.")

    market_num = 1 if market == "bours" else 2
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.53'
    }
    url = f"https://cdn.tsetmc.com/api/Instrument/GetInstrumentOptionMarketWatch/{market_num}"
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, headers=headers) as response:
                response.raise_for_status()
                json_response = await response.json()
                data = json_response.get('instrumentOptMarketWatch', [])
                eta = time.time() - start_time
                print(f"eta for {market}: {eta}")
                return data
        except (requests.RequestException, ValueError) as e:
            print(f"An error occurred while fetching option data: {e}")
            return []


async def get_total_option_data() -> List[dict]:
    start_time = time.time()
    result = await asyncio.gather(
        get_option_data("bours"),
        get_option_data("fara_bours")
    )
    bours, fara_bours = result
    total = bours + fara_bours
    eta = time.time() - start_time
    print(f"eta for total: {eta}")
    return total


def clean_total_option_data(raw_data: List[dict]) -> pd.DataFrame:
    df = pd.DataFrame(raw_data)
    general_columns = [column for column in df.columns if (not column.endswith("_P")) and (not column.endswith("_C"))]
    specific_columns = [column.replace("_C", "") for column in df.columns if column.endswith("_C")]

    calls = df[general_columns + [column + "_C" for column in specific_columns]]
    calls.columns = [column.replace("_C", "") for column in calls.columns]
    calls = calls.rename(columns=specific_columns_name)
    calls['option_type'] = 'call'

    puts = df[general_columns + [column + "_P" for column in specific_columns]]
    puts.columns = [column.replace("_P", "") for column in puts.columns]
    puts = puts.rename(columns=specific_columns_name)
    puts['option_type'] = 'put'

    # Concatenate the calls and puts DataFrames
    result_df = pd.concat([calls, puts], ignore_index=True)
    result_df.rename(columns=general_columns_name, inplace=True)
    return result_df


def get_cleaned_options_data() -> pd.DataFrame:
    raw_data = asyncio.run(get_total_option_data())
    clean_df = clean_total_option_data(raw_data)
    return clean_df


if __name__ == "__main__":
    clean_data = get_cleaned_options_data()
    print(clean_data)
