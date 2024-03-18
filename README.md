# TSELiveOptionData
This repository contains code to fetch and process live option data from the Tehran Stock Exchange (TSE). 
The main function in `third_parties/tsetmc.py` is `get_cleaned_options_data`, which retrieves option data from the TSE API and cleans it for further analysis.

## Example Usage
The `screen_market.py` file in this repository serves as an example that demonstrates the use case of the `get_cleaned_options_data` function. 
It showcases how to create an instance of the `OptionMarket` class, analyze option market data, and print out various metrics related to option trading.

## Note
* The code uses the TSE API to retrieve live option data. Make sure you have a stable internet connection.
* The code assumes the availability of the `pandas` and `requests` libraries. Install them if not already installed.

