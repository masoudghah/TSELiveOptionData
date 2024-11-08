# TSELiveOptionData

----
This repository contains code for fetching and processing live option data from various public APIs.



## How to Use This Repository

---

First, ensure that you have Python version 3.12 or higher installed. After that, you must install the dependencies with the following command:

`pip install -r requirements.txt`

## Project Structure

---
The project consists of two main directories: `data_source` and `use_case`. The `data_source` directory contains code for interacting with public APIs, while the `use_case` directory includes independent modules that utilize raw data from the data sources.



## Data Sources

---
| Source            | Description                                                                                                                                    | File                        | Data Example                                                                                     |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|--------------------------------------------------------------------------------------------------|
| TSETMC Website    |Fetches all Bourse and FaraBours data (suitable for screening the total market).                                                               | `data_source/tsetmc/api.py` | `data_source/tsetmc/TSETMC_sample_data.csv`                                                      |
| Tadbir Public API | Provides low latency and more detailed data (such as initial margin and order book). This may be suitable for obtaining data for actual trading. | `data_source/tadbir/api.py` | `data_source/tadbir/tadbir_detail_data_sample.json`, `data_source/tadbir/Tadbir_sample_data.csv` |



## Use cases

---

Currently, this directory contains only one module, `screen_market.py`, but it will be expanded in the future!



### screen_market
The `screen_market.py` file serves as an example demonstrating the use case of the TSETMC website data. It showcases how to create an instance of the `OptionMarket` class, analyze option market data, and print various metrics related to option trading.




## Technical Terms

---

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
