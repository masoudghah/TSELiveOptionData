# tseopt

This library contains code for fetching and processing option data from the Tehran Stock Exchange using various public APIs.

---
## Requirements
### 1. Ensure Python version **3.12** or higher is installed

Check if Python is installed and available from the command line by running:

```bash
python3 --version # Unix/macOS
```
or
```bash
py --version # Windows
```
If you do not have Python, please install the **latest** 3.x version from python.org 


### 2. Ensure you can run pip from the command line

```bash
python3 -m pip --version # Unix/macOS
```
or

```bash
py -m pip --version # Windows
```

If pip isn’t already installed, then first try to bootstrap it from the standard library:
```bash
python3 -m ensurepip --default-pip  # Unix/macOS
```
or

```bash
py -m ensurepip --default-pip # Windows
```

### 3. Create a Virtual Environment
Now that you have Python and pip set up, you can create a virtual environment. 
Navigate to your project directory and run the following command:
```bash
python3 -m venv venv  # Unix/macOS
```
or

```bash
py -m venv venv # Windows
```

### 4. Activate the Virtual Environment

Next, you need to activate the virtual environment:
```bash
source venv/bin/activate  # Unix/macOS
```
or

```bash
venv\Scripts\activate # Windows
```

After activation, your command prompt should change to indicate that you are now working within the virtual environment.


### 5. Upgrade pip, setuptools, and wheel

```bash
python3 -m pip install --upgrade pip setuptools wheel # Unix/macOS
```
or
```bash
py -m pip install --upgrade pip setuptools wheel # Windows
```
---

## Installation

Use the package manager pip to install `tseopt`.

```bash
pip install tseopt
```

## Usage
##### For a better view of the output data, please refer to `README.ipynb`.


### TSETMC Website API
Fetches all Bourse and FaraBours data (suitable for screening the total market).
```python
from tseopt import get_all_options_data

entire_option_market_data = get_all_options_data()
print(entire_option_market_data.head(5))
print(entire_option_market_data.iloc[0])

```

### Screen Market

```python
import pandas as pd
from tseopt.use_case.screen_market import OptionMarket, convert_to_billion_toman

option_market = OptionMarket(entire_option_market_data=entire_option_market_data)

print(f"total_trade_value: {option_market.total_trade_value / 1e10:.0f} B Toman", end="\n\n")

most_trade_value_calls = pd.DataFrame(option_market.most_trade_value.get("call"))
most_trade_value_calls['ticker'] = most_trade_value_calls['ticker'].astype(str)
most_trade_value_calls["trades_value"] = convert_to_billion_toman(most_trade_value_calls["trades_value"])


most_trade_value_puts = pd.DataFrame(option_market.most_trade_value.get("put"))
most_trade_value_puts['ticker'] = most_trade_value_puts['ticker'].astype(str)
most_trade_value_puts["trades_value"] = convert_to_billion_toman(most_trade_value_puts["trades_value"])


most_trade_value_by_underlying_asset = pd.DataFrame(option_market.most_trade_value_by_underlying_asset)
most_trade_value_by_underlying_asset[["call", "put", "total"]] =convert_to_billion_toman(most_trade_value_by_underlying_asset[["call", "put", "total"]])


print(most_trade_value_calls)
print(most_trade_value_puts)
print(most_trade_value_by_underlying_asset)

```

### Tadbir API
Provides low latency and more detailed data (such as initial margin and order book). This may be suitable for obtaining data for actual trading.
```python
from tseopt import tadbir_api

isin_list = ["IRO9AHRM2501", "IROATVAF0621", "IRO9BMLT2771", "IRO9TAMN8991", "IRO9IKCO81M1"]

bulk_data = tadbir_api.get_last_bulk_data(isin_list=isin_list)
detail_data = tadbir_api.get_detail_data(isin_list[0])
symbol_info = detail_data.get("symbol_info")
order_book = pd.DataFrame(detail_data.get("order_book"))

print(bulk_data)

print(symbol_info)
print(order_book)

```

### Mercantile Exchange
Fetches all data which mercantile exchange website provides.
```python
from tseopt import make_a_mercantile_data_object


md = make_a_mercantile_data_object()
md.update_data(timeout=20)
print(md.gavahi[0])
print(md.sandoq[0])
print(md.salaf[0])
print(md.future[0])
print(md.markets_info[0])
print(md.cdc[0])
print(md.all_market)
print(md.future_date_time)

```

### Technical Terms


| English Word           | Farsi Translation           |
|-----------------------|-----------------------------|
| ua_tse_code           | کد نماد دارایی پایه         |
| ua_ticker             | نماد معاملاتی دارایی پایه   |
| days_to_maturity      | روزهای باقی‌مانده تا سررسید |
| strike_price          | قیمت اعمال                  |
| contract_size         | اندازه قرارداد              |
| ua_close_price        | قیمت پایانی دارایی پایه     |
| ua_yesterday_price    | قیمت روز گذشته دارایی پایه  |
| begin_date            | تاریخ شروع قرارداد          |
| end_date              | تاریخ سررسید قرارداد        |
| tse_code              | کد نماد آپشن                |
| ticker                | نماد معاملاتی آپشن              |
| trades_num            | تعداد معاملات آپشن              |
| trades_volume         | حجم معاملات آپشن                |
| trades_value          | ارزش معاملات آپشن               |
| last_price            | آخرین قیمت آپشن                 |
| close_price           | قیمت پایانی آپشن                |
| yesterday_price       | قیمت روز گذشته آپشن             |
| open_positions        | موقعیت‌های باز              |
| yesterday_open_positions | موقعیت‌های باز روز گذشته    |
| notional_value        | ارزش اسمی                   |
| bid_price             | قیمت پیشنهادی خرید          |
| bid_volume            | حجم پیشنهادی خرید           |
| ask_price             | قیمت پیشنهادی فروش          |
| ask_volume            | حجم پیشنهادی فروش           |


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)