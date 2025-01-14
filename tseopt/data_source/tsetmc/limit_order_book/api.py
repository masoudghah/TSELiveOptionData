from datetime import time, date

import jdatetime
import pandas as pd
import requests

from tseopt.data_source.tsetmc.limit_order_book.schemas import RawLOBLevel, columns_name


def convert_to_time_format(time_value: int) -> time:
    """
    Convert an integer in HHMMSS format to a time object.

    Parameters:
    ----------
    time_value : int
        An integer representing time in HHMMSS format.

    Returns:
    -------
    time
        A time object corresponding to the input integer.

    Examples:
    --------
    >>> convert_to_time_format(123456)
    datetime.time(12, 34, 56)
    """
    time_str = str(time_value).zfill(6)
    return pd.to_datetime(time_str, format='%H%M%S').time()


def fetch_lob_data(tse_code: str, date: str) -> list[RawLOBLevel]:
    """
    Fetch the limit order book data for a given TSE code and date.

    Parameters:
    ----------
    tse_code : str
        The TSE code for which to fetch the order book data.
    date : str
        The date for which to fetch the order book data in YYYYMMDD format.

    Returns:
    -------
    List[RawLOBLevel]
        A list of RawLOBLevel dictionaries containing the order book data.

    Raises:
    ------
    ValueError
        If the response does not contain valid order book data.

    Examples:
    ---------
    >>> date = "20241218"
    >>> ua_tse_code = "17914401175772326"
    >>> lob_data = fetch_lob_data(ua_tse_code, date)
    >>> print(lob_data)
    [{'idn': 1, 'dEven': 20241218, 'hEven': 60127, 'refID': 13224976709, 
      'number': 4, 'qTitMeDem': 20000, 'zOrdMeDem': 1, 'pMeDem': 25060.0, 
      'pMeOf': 26480.0, 'zOrdMeOf': 1, 'qTitMeOf': 9880, 'insCode': None}, 
     {'idn': 2, 'dEven': 20241218, 'hEven': 60128, 'refID': 13224976710, 
      'number': 5, 'qTitMeDem': 15000, 'zOrdMeDem': 2, 'pMeDem': 25050.0, 
      'pMeOf': 26490.0, 'zOrdMeOf': 2, 'qTitMeOf': 8000, 'insCode': None}, ...]
    """
    url = f"https://cdn.tsetmc.com/api/BestLimits/{tse_code}/{date}"

    response = requests.get(url)
    response.raise_for_status()

    json_response = response.json()
    order_book_data = json_response.get("bestLimitsHistory")

    if order_book_data is None:
        raise ValueError("No order book data found in the response.")

    if not order_book_data:
        raise ValueError("No order book data available for the specified date.")

    return order_book_data


def process_raw_data(raw_data: list[RawLOBLevel]) -> pd.DataFrame:
    data = pd.DataFrame(raw_data)
    data.rename(columns=columns_name, inplace=True)
    data['time'] = data['hEven'].apply(convert_to_time_format)
    columns = list(columns_name.values()) + ["time"]
    return data[columns].sort_values(by=["time", "level"]).reset_index(drop=True)


class HistoricalLOBInput:
    def __init__(self, tse_code: str, jalali_date: str) -> None:
        """
        Parameters:
        ----------
        tse_code : str
            The TSE code for the financial instrument.
        jalali_date : str
            The Jalali date in the format 'YYYY-MM-DD'.

        Raises:
        -------
        ValueError
            If the provided Jalali date is invalid or not a trading day.
        """
        self.tse_code = tse_code
        self.date = self.jalali_to_gregorian(jalali_date)

    def jalali_to_gregorian(self, jalali_date: str) -> str:
        """
        Convert a Jalali date to a Gregorian date and check if it is a trading day.

        Parameters:
        ----------
        jalali_date : str
            The Jalali date in the format 'YYYY-MM-DD'.

        Returns:
        -------
        str
            The corresponding Gregorian date in the format 'YYYYMMDD'.

        Raises:
        -------
        ValueError
            If the date does not fall on a trading day.
        """
        year, month, day = map(int, jalali_date.split('-'))
        jalali_date_obj = jdatetime.date(year, month, day)

        # Convert to Gregorian date
        gregorian_date_obj = jalali_date_obj.togregorian()

        # Validate the trading day
        self.validate_date(gregorian_date_obj)

        return gregorian_date_obj.strftime('%Y%m%d')

    @staticmethod
    def validate_date(gregorian_date: date) -> None:
        """
        Validate if the given Gregorian date is a trading day.

        Parameters:
        ----------
        gregorian_date : date
            The Gregorian date to validate.

        Raises:
        -------
        ValueError
            If the date is not a trading day (Saturday to Wednesday).
        """
        weekday = gregorian_date.weekday()
        if weekday not in [5, 0, 1, 2]:  # Saturday (5), Sunday (6), Monday (0), Tuesday (1), Wednesday (2)
            raise ValueError("The date is not a trading day.")


def fetch_historical_lob(*, tse_code: str, jalali_date: str) -> pd.DataFrame:
    """
    Parameters:
    ----------
    tse_code : str
        The TSE code for the financial instrument.
    jalali_date : str
        The Jalali date in the format 'YYYY-MM-DD'.

    Raises:
    -------
    ValueError
        If the provided Jalali date is invalid or not a trading day.
    """
    inp = HistoricalLOBInput(tse_code=tse_code, jalali_date=jalali_date)
    raw_data = fetch_lob_data(inp.tse_code, inp.date)
    return process_raw_data(raw_data)


def take_lob_screenshot(entire_data: pd.DataFrame, specific_time: str) -> pd.DataFrame:
    """
    Parameters:
    ----------
    lob : pd.DataFrame
        The output of the fetch_historical_lob function.
    specific_time : str
        The specific time in 'HH:MM' format.

    Returns:
    -------
    pd.DataFrame

    """
    specific_time += ":00"
    specific_time_obj = pd.to_datetime(specific_time).time()

    filter_lob = entire_data[entire_data["time"] <= specific_time_obj]
    return filter_lob.groupby('level').last().reset_index()


if __name__ == "__main__":
    jalali_date = "1403-10-24"
    tse_code = "17091434834979599"
    specific_time = "10:50"

    data = fetch_historical_lob(tse_code=tse_code, jalali_date=jalali_date)
    lob = take_lob_screenshot(entire_data=data, specific_time=specific_time)
    # print(data)
    print(lob.to_string())


