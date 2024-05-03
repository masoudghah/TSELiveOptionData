# TSELiveOptionData
This repository contains code for fetching and processing live option data from various public APIs.

----
## TSETMC Source
The primary function in` third_parties/tsetmc.py` is `get_cleaned_options_data`, which fetches option data from the TSETMC API and preprocesses it for further analysis. An example of the output from this source can be found in `data.csv`.



* ### Example Usage
The `screen_market.py` file in this repository serves as an example that demonstrates the use case of the `get_cleaned_options_data` function. 
It showcases how to create an instance of the `OptionMarket` class, analyze option market data, and print out various metrics related to option trading.

---

## Tadbir Source
The Tadbir source provides low latency and more detailed data related to the TSETMC API. If the TSETMC API is suitable for screening the total market, then Tadbir may be suitable for obtaining data for actual trading. The Tadbir source offers two endpoints:

1. For retrieving data in bulk (refer to the example output in `tadbir_bulk_data_sample.csv`).
2. For obtaining specific symbol information (such as initial margin) and its order book (refer to the example output in `tadbir_detail_data_sample.json`).

## Note
* The code utilizes APIs to fetch live option data. Ensure you have a stable internet connection.
* The code assumes the availability of the `pandas` and `requests` libraries. Install them if not already installed.

