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
| Source            | Description                                                                                                                                    |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| TSETMC Website    |Fetches all Bourse and FaraBours data (suitable for screening the total market).                                                               |
| Tadbir Public API | Provides low latency and more detailed data (such as initial margin and order book). This may be suitable for obtaining data for actual trading. |



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


# Usage


```python
from IPython.display import display
import pandas as pd
```

# TSETMC Website API


```python
from data_source.tsetmc.api import fetch_cleaned_entire_market_data

read_data_from_file = True
read_data_from_file = False

csv_file_path = r"data_source\tsetmc\TSETMC_sample_data.csv"

if read_data_from_file:
    entire_option_market_data = pd.read_csv(csv_file_path)
else:
    entire_option_market_data = fetch_cleaned_entire_market_data()
    entire_option_market_data.to_csv(path_or_buf=csv_file_path, index=False)


display(entire_option_market_data)
print(entire_option_market_data.iloc[0])
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>contract_size</th>
      <th>ua_tse_code</th>
      <th>ua_ticker</th>
      <th>ua_close_price</th>
      <th>ua_yesterday_price</th>
      <th>begin_date</th>
      <th>end_date</th>
      <th>strike_price</th>
      <th>days_to_maturity</th>
      <th>tse_code</th>
      <th>...</th>
      <th>trades_volume</th>
      <th>trades_num</th>
      <th>name</th>
      <th>ticker</th>
      <th>bid_price</th>
      <th>bid_volume</th>
      <th>ask_price</th>
      <th>ask_volume</th>
      <th>yesterday_open_positions</th>
      <th>option_type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1000</td>
      <td>17914401175772326</td>
      <td>اهرم</td>
      <td>16850</td>
      <td>16680</td>
      <td>20240615</td>
      <td>20241120</td>
      <td>13000</td>
      <td>7</td>
      <td>28659628629467662</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>اختيارخ اهرم-13000-1403/08/30</td>
      <td>ضهرم8000</td>
      <td>3030</td>
      <td>1</td>
      <td>4000</td>
      <td>50</td>
      <td>771</td>
      <td>call</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1000</td>
      <td>17914401175772326</td>
      <td>اهرم</td>
      <td>16850</td>
      <td>16680</td>
      <td>20240615</td>
      <td>20241120</td>
      <td>28000</td>
      <td>7</td>
      <td>44178602874527907</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>اختيارخ اهرم-28000-1403/08/30</td>
      <td>ضهرم8009</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>call</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1000</td>
      <td>17914401175772326</td>
      <td>اهرم</td>
      <td>16850</td>
      <td>16680</td>
      <td>20240615</td>
      <td>20241120</td>
      <td>34000</td>
      <td>7</td>
      <td>22708611335290724</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>اختيارخ اهرم-34000-1403/08/30</td>
      <td>ضهرم8011</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>call</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1000</td>
      <td>17914401175772326</td>
      <td>اهرم</td>
      <td>16850</td>
      <td>16680</td>
      <td>20240720</td>
      <td>20241218</td>
      <td>34000</td>
      <td>35</td>
      <td>19782620412160557</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>اختيارخ اهرم-34000-1403/09/28</td>
      <td>ضهرم9011</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>call</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1000</td>
      <td>17914401175772326</td>
      <td>اهرم</td>
      <td>16850</td>
      <td>16680</td>
      <td>20240824</td>
      <td>20250115</td>
      <td>15000</td>
      <td>63</td>
      <td>8825940836055699</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>اختيارخ اهرم-15000-1403/10/26</td>
      <td>ضهرم1005</td>
      <td>2211</td>
      <td>204</td>
      <td>2597</td>
      <td>48</td>
      <td>5688</td>
      <td>call</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2001</th>
      <td>1000</td>
      <td>69067576215760005</td>
      <td>كاريس</td>
      <td>24498</td>
      <td>24431</td>
      <td>20240731</td>
      <td>20241201</td>
      <td>30000</td>
      <td>18</td>
      <td>50721610494714355</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>اختيارف كاريس-30000-14030911</td>
      <td>طكاريس913</td>
      <td>1</td>
      <td>25</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>put</td>
    </tr>
    <tr>
      <th>2002</th>
      <td>1000</td>
      <td>41927452991671109</td>
      <td>توان</td>
      <td>16631</td>
      <td>16598</td>
      <td>20240706</td>
      <td>20241222</td>
      <td>13000</td>
      <td>39</td>
      <td>40401356882294435</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>اختيارف توان-13000-14031002</td>
      <td>طتوان1002</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>put</td>
    </tr>
    <tr>
      <th>2003</th>
      <td>1000</td>
      <td>41927452991671109</td>
      <td>توان</td>
      <td>16631</td>
      <td>16598</td>
      <td>20240706</td>
      <td>20241222</td>
      <td>15000</td>
      <td>39</td>
      <td>10977288290284133</td>
      <td>...</td>
      <td>400</td>
      <td>4</td>
      <td>اختيارف توان-15000-14031002</td>
      <td>طتوان1004</td>
      <td>430</td>
      <td>200</td>
      <td>460</td>
      <td>200</td>
      <td>6971</td>
      <td>put</td>
    </tr>
    <tr>
      <th>2004</th>
      <td>1000</td>
      <td>41927452991671109</td>
      <td>توان</td>
      <td>16631</td>
      <td>16598</td>
      <td>20240706</td>
      <td>20241222</td>
      <td>18000</td>
      <td>39</td>
      <td>45072004043727679</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>اختيارف توان-18000-14031002</td>
      <td>طتوان1007</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>27</td>
      <td>put</td>
    </tr>
    <tr>
      <th>2005</th>
      <td>1000</td>
      <td>41927452991671109</td>
      <td>توان</td>
      <td>16631</td>
      <td>16598</td>
      <td>20240706</td>
      <td>20241222</td>
      <td>20000</td>
      <td>39</td>
      <td>29281123483357422</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>اختيارف توان-20000-14031002</td>
      <td>طتوان1009</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>put</td>
    </tr>
  </tbody>
</table>
<p>2006 rows × 26 columns</p>
</div>


    contract_size                                        1000
    ua_tse_code                             17914401175772326
    ua_ticker                                            اهرم
    ua_close_price                                      16850
    ua_yesterday_price                                  16680
    begin_date                                       20240615
    end_date                                         20241120
    strike_price                                        13000
    days_to_maturity                                        7
    tse_code                                28659628629467662
    last_price                                           3550
    open_positions                                        771
    close_price                                          3472
    yesterday_price                                      3472
    notional_value                                150120000.0
    trades_value                                          0.0
    trades_volume                                           0
    trades_num                                              0
    name                        اختيارخ اهرم-13000-1403/08/30
    ticker                                           ضهرم8000
    bid_price                                            3030
    bid_volume                                              1
    ask_price                                            4000
    ask_volume                                             50
    yesterday_open_positions                              771
    option_type                                          call
    Name: 0, dtype: object
    

# Screen Market


```python
from use_case.screen_market import OptionMarket, convert_to_billion_toman

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


display(most_trade_value_calls)
display(most_trade_value_puts)
display(most_trade_value_by_underlying_asset)
```

    total_trade_value: 268 B Toman
    
    


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ticker</th>
      <th>trades_value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>ضهرم9003</td>
      <td>65.1 B Toman</td>
    </tr>
    <tr>
      <th>1</th>
      <td>ضخود9027</td>
      <td>39.21 B Toman</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ضخود9026</td>
      <td>24.5 B Toman</td>
    </tr>
    <tr>
      <th>3</th>
      <td>ضهرم8003</td>
      <td>21.05 B Toman</td>
    </tr>
    <tr>
      <th>4</th>
      <td>ضخود9025</td>
      <td>8.68 B Toman</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ticker</th>
      <th>trades_value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>طهرم9003</td>
      <td>18.22 B Toman</td>
    </tr>
    <tr>
      <th>1</th>
      <td>طخود9027</td>
      <td>12.21 B Toman</td>
    </tr>
    <tr>
      <th>2</th>
      <td>طهرم8003</td>
      <td>3.86 B Toman</td>
    </tr>
    <tr>
      <th>3</th>
      <td>طخود9026</td>
      <td>3.36 B Toman</td>
    </tr>
    <tr>
      <th>4</th>
      <td>طهرم8004</td>
      <td>2.74 B Toman</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ua_ticker</th>
      <th>call</th>
      <th>put</th>
      <th>total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>اهرم</td>
      <td>102.82 B Toman</td>
      <td>29.41 B Toman</td>
      <td>132.23 B Toman</td>
    </tr>
    <tr>
      <th>1</th>
      <td>خودرو</td>
      <td>92.63 B Toman</td>
      <td>16.43 B Toman</td>
      <td>109.06 B Toman</td>
    </tr>
    <tr>
      <th>2</th>
      <td>شستا</td>
      <td>7.76 B Toman</td>
      <td>0.44 B Toman</td>
      <td>8.2 B Toman</td>
    </tr>
    <tr>
      <th>3</th>
      <td>توان</td>
      <td>4.22 B Toman</td>
      <td>0.05 B Toman</td>
      <td>4.26 B Toman</td>
    </tr>
    <tr>
      <th>4</th>
      <td>خساپا</td>
      <td>4.0 B Toman</td>
      <td>0.0 B Toman</td>
      <td>4.0 B Toman</td>
    </tr>
  </tbody>
</table>
</div>


# Tadbir API


```python
from data_source.tadbir.api import tadbir_api

from pprint import pprint

isin_list = ["IRO9AHRM2501", "IROATVAF0621", "IRO9BMLT2771", "IRO9TAMN8991", "IRO9IKCO81M1"]

bulk_data = tadbir_api.get_last_bulk_data(isin_list=isin_list)
detail_data = tadbir_api.get_detail_data(isin_list[0])
symbol_info = detail_data.get("symbol_info")
order_book = pd.DataFrame(detail_data.get("order_book"))

display(bulk_data)

pprint(symbol_info)
display(order_book)


```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>BasisVolume</th>
      <th>ClosingPrice</th>
      <th>CompanyName</th>
      <th>BestBuyPrice</th>
      <th>BestBuyQuantity</th>
      <th>BestSellPrice</th>
      <th>BestSellQuantity</th>
      <th>NoBestBuy</th>
      <th>NoBestSell</th>
      <th>FirstTradedPrice</th>
      <th>...</th>
      <th>TotalTradeValue</th>
      <th>TradeDate</th>
      <th>varSign</th>
      <th>ClosingPriceVar</th>
      <th>ClosingPriceVarPercent</th>
      <th>LastTradedPriceVar</th>
      <th>LastTradedPriceVarPercent</th>
      <th>tse_code</th>
      <th>SectorCodeId</th>
      <th>cs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>1999.0</td>
      <td>اختیارخ اهرم-16000-1403/11/24</td>
      <td>1506.0</td>
      <td>2</td>
      <td>1989.0</td>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>1999.0</td>
      <td>...</td>
      <td>39980000.0</td>
      <td>1403/8/22 9:40</td>
      <td>1</td>
      <td>201.0</td>
      <td>11.18</td>
      <td>201.0</td>
      <td>11.18</td>
      <td>18154069997422059</td>
      <td>None</td>
      <td>1000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.0</td>
      <td>1241.0</td>
      <td>اختیارخ توان-16000-14031002</td>
      <td>1300.0</td>
      <td>57</td>
      <td>1320.0</td>
      <td>43</td>
      <td>1</td>
      <td>1</td>
      <td>1200.0</td>
      <td>...</td>
      <td>505234000.0</td>
      <td>1403/8/22 10:13</td>
      <td>0</td>
      <td>-64.0</td>
      <td>-4.90</td>
      <td>15.0</td>
      <td>1.15</td>
      <td>14732757416991570</td>
      <td>None</td>
      <td>1000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1.0</td>
      <td>355.0</td>
      <td>اختیارخ وبملت-1800-1403/11/24</td>
      <td>177.0</td>
      <td>1</td>
      <td>665.0</td>
      <td>55</td>
      <td>1</td>
      <td>1</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>1403/8/14 12:26</td>
      <td>1</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>48841241645050970</td>
      <td>None</td>
      <td>1000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1.0</td>
      <td>98.0</td>
      <td>اختیارخ شستا-850-1403/08/09</td>
      <td>0.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>1403/8/9 12:29</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>18794200601794224</td>
      <td>None</td>
      <td>1000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1.0</td>
      <td>1.0</td>
      <td>اختیارخ خودرو-4000-1403/03/09</td>
      <td>0.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>1403/3/9 10:29</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>414085078149021</td>
      <td>None</td>
      <td>1000</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 38 columns</p>
</div>


    {'BaseVolume': 1,
     'CP12': 1999,
     'ClosingPrice': 1999.0,
     'CompanyTitle': 'اختیارخ اهرم-16000-1403/11/24',
     'GroupStateID': 5,
     'HighAllowedPrice': 500000.0,
     'HighPrice': 0.0,
     'InstrumentCode': '18154069997422059',
     'IsCautionAgreement': False,
     'IsSepahAgreement': False,
     'LastTradedPrice': 1999.0,
     'LotSize': 1,
     'LowAllowedPrice': 1.0,
     'LowPercent': 100,
     'LowPrice': 0.0,
     'MarketType': 'MarketType.BuyOption',
     'MaxPercent': 27709,
     'MaxQuantityOrder': 1000,
     'MinQuantityOrder': 1,
     'NSCCode': 'IRO9AHRM2501',
     'RefPrice': 1798.0,
     'Symbol': 'ضهرم1105',
     'SymbolStateId': 1,
     'TickSize': 1.0,
     'TotalNumberOfSharesTraded': 20,
     'TotalNumberOfTrades': 1,
     'TotalTradeValue': 39980000.0,
     'TradeDate': '1403/08/22 - 09:40:53',
     'UA_LastTradedPrice': 16830.0,
     'UA_isin': 'IRT1AHRM0001',
     'YesterdayPrice': 1798.0,
     'contractSize': 1000,
     'contractStartDate': '1403/07/01',
     'cpv': 201.0,
     'cpvp': 11.18,
     'crn': 'ریال',
     'crp': 1,
     'exerciseDate': '1403/11/24',
     'gc': '3A',
     'initial_margin': 3360000.0,
     'iso': True,
     'lpv': 201.0,
     'lpvp': 11.18,
     'mbop': 0,
     'mcaop': 112000,
     'mcop': 112000,
     'mmop': 2250000,
     'openPositionNum': 5712,
     'pv': 11.18,
     'rm': 5359000.0,
     'strikePrice': 16000.0,
     'th': 555901.0,
     'tl': 0.0,
     'vs': 1}
    


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>BestBuyPrice</th>
      <th>BestSellPrice</th>
      <th>BestSellQuantity</th>
      <th>BestBuyQuantity</th>
      <th>NoBestBuy</th>
      <th>NoBestSell</th>
      <th>NSCCode</th>
      <th>Place</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1506.0</td>
      <td>1989.0</td>
      <td>4</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>IRO9AHRM2501</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1505.0</td>
      <td>1990.0</td>
      <td>66</td>
      <td>100</td>
      <td>1</td>
      <td>1</td>
      <td>IRO9AHRM2501</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1504.0</td>
      <td>2000.0</td>
      <td>500</td>
      <td>16</td>
      <td>3</td>
      <td>1</td>
      <td>IRO9AHRM2501</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1503.0</td>
      <td>2099.0</td>
      <td>20</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>IRO9AHRM2501</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1502.0</td>
      <td>2480.0</td>
      <td>2</td>
      <td>210</td>
      <td>2</td>
      <td>1</td>
      <td>IRO9AHRM2501</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>


# Mercantile Exchange


```python
from data_source.mercantile_exchange.api import make_a_mercantile_exchange_object


mercantile_exchange = make_a_mercantile_exchange_object()
res = mercantile_exchange.get_data(timeout=20)
```


```python
from IPython.display import display
import pandas as pd

for market in res:
    title = market["M"]
    data = market["A"][0]
    if isinstance(data, list):
        df = pd.DataFrame(data)
        print(title)
        display(df)
        print("\n\n")

        # df.to_csv(title+".csv", index=False)
    else:
        print(title)
        print(data, end="\n\n")

```

    updateGavahiMarketsInfo
    


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>Code</th>
      <th>Symbol</th>
      <th>Name</th>
      <th>YesterdayPrice</th>
      <th>FinalPrice</th>
      <th>LastPrice</th>
      <th>PriceChange</th>
      <th>FirstPrice</th>
      <th>MinPrice</th>
      <th>...</th>
      <th>Buy_CountI</th>
      <th>Buy_CountN</th>
      <th>Buy_I_Volume</th>
      <th>Buy_N_Volume</th>
      <th>Sell_CountI</th>
      <th>Sell_CountN</th>
      <th>Sell_I_Volume</th>
      <th>Sell_N_Volume</th>
      <th>ModifyDate</th>
      <th>ModifyTime</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>16255851958781005</td>
      <td>IRK1K01103C4</td>
      <td>سكه0312پ01</td>
      <td>تمام سكه طرح جديد0312 رفاه</td>
      <td>4941360.0</td>
      <td>4964567.0</td>
      <td>4970000.0</td>
      <td>28640.0</td>
      <td>4958777.0</td>
      <td>4944501.0</td>
      <td>...</td>
      <td>235</td>
      <td>0</td>
      <td>115100.0</td>
      <td>0.0</td>
      <td>173</td>
      <td>2</td>
      <td>88700.0</td>
      <td>26400.0</td>
      <td>0001-01-01T00:00:00</td>
      <td>15:02:01</td>
    </tr>
    <tr>
      <th>1</th>
      <td>31447590411939048</td>
      <td>IRK1K01704C9</td>
      <td>سكه0412پ03</td>
      <td>تمام سكه طرح جديد0412 سامان</td>
      <td>4940567.0</td>
      <td>4979430.0</td>
      <td>4970002.0</td>
      <td>29435.0</td>
      <td>4984955.0</td>
      <td>4951155.0</td>
      <td>...</td>
      <td>53</td>
      <td>1</td>
      <td>14500.0</td>
      <td>109000.0</td>
      <td>33</td>
      <td>1</td>
      <td>9100.0</td>
      <td>114400.0</td>
      <td>0001-01-01T00:00:00</td>
      <td>15:02:01</td>
    </tr>
    <tr>
      <th>2</th>
      <td>62180931969029505</td>
      <td>IRK1K01604B3</td>
      <td>سكه0411پ05</td>
      <td>تمام سكه طرح جديد0411 آينده</td>
      <td>4939362.0</td>
      <td>4979204.0</td>
      <td>4978970.0</td>
      <td>39608.0</td>
      <td>4962500.0</td>
      <td>4950155.0</td>
      <td>...</td>
      <td>34</td>
      <td>1</td>
      <td>6100.0</td>
      <td>109000.0</td>
      <td>33</td>
      <td>1</td>
      <td>6800.0</td>
      <td>108300.0</td>
      <td>0001-01-01T00:00:00</td>
      <td>15:00:46</td>
    </tr>
    <tr>
      <th>3</th>
      <td>61915698210562012</td>
      <td>IRK1A11004A8</td>
      <td>زعف0410پ11</td>
      <td>زعفران0410نگين سحرخيز(پ)</td>
      <td>828699.0</td>
      <td>834697.0</td>
      <td>835000.0</td>
      <td>6301.0</td>
      <td>834398.0</td>
      <td>826000.0</td>
      <td>...</td>
      <td>32</td>
      <td>1</td>
      <td>104919.0</td>
      <td>44419.0</td>
      <td>47</td>
      <td>1</td>
      <td>149138.0</td>
      <td>200.0</td>
      <td>0001-01-01T00:00:00</td>
      <td>15:02:01</td>
    </tr>
    <tr>
      <th>4</th>
      <td>53891388774506731</td>
      <td>IRK1A11404A0</td>
      <td>زعف0410پ08</td>
      <td>زعفران0410نگين روستا(پ)</td>
      <td>821382.0</td>
      <td>854641.0</td>
      <td>863441.0</td>
      <td>42059.0</td>
      <td>825000.0</td>
      <td>825000.0</td>
      <td>...</td>
      <td>0</td>
      <td>1</td>
      <td>0.0</td>
      <td>115000.0</td>
      <td>12</td>
      <td>0</td>
      <td>115000.0</td>
      <td>0.0</td>
      <td>0001-01-01T00:00:00</td>
      <td>14:54:35</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>62</th>
      <td>53166825580151724</td>
      <td>IRK1A10803A4</td>
      <td>زعف0310پ22</td>
      <td>زعفران0310نگين گليران(پ)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0001-01-01T00:00:00</td>
      <td>13:07:48</td>
    </tr>
    <tr>
      <th>63</th>
      <td>13489302489605681</td>
      <td>IRK1A11904A9</td>
      <td>زعف0410پ21</td>
      <td>زعفران0410نگين ملل(پ)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0001-01-01T00:00:00</td>
      <td>14:54:35</td>
    </tr>
    <tr>
      <th>64</th>
      <td>68063545647106529</td>
      <td>IRK1A10903A2</td>
      <td>زعف0310پ08</td>
      <td>زعفران0310نگين روستا(پ)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0001-01-01T00:00:00</td>
      <td>11:05:10</td>
    </tr>
    <tr>
      <th>65</th>
      <td>64352308103866382</td>
      <td>IRK1A10703A6</td>
      <td>زعف0310پ21</td>
      <td>زعفران0310نگين ملل(پ)</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0001-01-01T00:00:00</td>
      <td>14:07:13</td>
    </tr>
    <tr>
      <th>66</th>
      <td>1626855364269097</td>
      <td>IRK1K01002B0</td>
      <td>سكه0211پ02</td>
      <td>تمام سكه طرح جديد0211ملت</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0001-01-01T00:00:00</td>
      <td>08:35:10</td>
    </tr>
  </tbody>
</table>
<p>67 rows × 56 columns</p>
</div>


    
    
    
    updateSandoqMarketsInfo
    


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>Code</th>
      <th>Symbol</th>
      <th>Name</th>
      <th>YesterdayPrice</th>
      <th>FinalPrice</th>
      <th>LastPrice</th>
      <th>PriceChange</th>
      <th>FirstPrice</th>
      <th>MinPrice</th>
      <th>...</th>
      <th>Buy_CountI</th>
      <th>Buy_CountN</th>
      <th>Buy_I_Volume</th>
      <th>Buy_N_Volume</th>
      <th>Sell_CountI</th>
      <th>Sell_CountN</th>
      <th>Sell_I_Volume</th>
      <th>Sell_N_Volume</th>
      <th>ModifyDate</th>
      <th>ModifyTime</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>34144395039913458</td>
      <td>IRTKMOFD0006</td>
      <td>عيار</td>
      <td>صندوق طلاي عيار مفيد</td>
      <td>123298.0</td>
      <td>123885.0</td>
      <td>124499.0</td>
      <td>1201.0</td>
      <td>123727.0</td>
      <td>123550.0</td>
      <td>...</td>
      <td>6075</td>
      <td>19</td>
      <td>25932288.0</td>
      <td>5641742.0</td>
      <td>3109</td>
      <td>5</td>
      <td>19708687.0</td>
      <td>11865343.0</td>
      <td>0001-01-01T00:00:00</td>
      <td>15:02:01</td>
    </tr>
    <tr>
      <th>1</th>
      <td>46700660505281786</td>
      <td>IRTKLOTF0009</td>
      <td>طلا</td>
      <td>صندوق س.پشتوانه طلاي لوتوس</td>
      <td>326048.0</td>
      <td>327644.0</td>
      <td>328999.0</td>
      <td>2951.0</td>
      <td>327505.0</td>
      <td>326500.0</td>
      <td>...</td>
      <td>3634</td>
      <td>13</td>
      <td>4845957.0</td>
      <td>295800.0</td>
      <td>1871</td>
      <td>5</td>
      <td>4192362.0</td>
      <td>949395.0</td>
      <td>0001-01-01T00:00:00</td>
      <td>15:02:01</td>
    </tr>
    <tr>
      <th>2</th>
      <td>25559236668122210</td>
      <td>IRTKROBA0008</td>
      <td>كهربا</td>
      <td>صندوق س.پشتوانه سكه طلا كهربا</td>
      <td>43320.0</td>
      <td>43451.0</td>
      <td>43683.0</td>
      <td>363.0</td>
      <td>43560.0</td>
      <td>43346.0</td>
      <td>...</td>
      <td>1960</td>
      <td>11</td>
      <td>19604557.0</td>
      <td>9749944.0</td>
      <td>897</td>
      <td>8</td>
      <td>13588827.0</td>
      <td>15765674.0</td>
      <td>0001-01-01T00:00:00</td>
      <td>15:02:01</td>
    </tr>
    <tr>
      <th>3</th>
      <td>32469128621155736</td>
      <td>IRTKZARA0006</td>
      <td>مثقال</td>
      <td>صندوق س.پشتوانه طلاي زرين آگاه</td>
      <td>36408.0</td>
      <td>36656.0</td>
      <td>36797.0</td>
      <td>389.0</td>
      <td>36551.0</td>
      <td>36551.0</td>
      <td>...</td>
      <td>1168</td>
      <td>3</td>
      <td>11366109.0</td>
      <td>640840.0</td>
      <td>633</td>
      <td>1</td>
      <td>11986949.0</td>
      <td>20000.0</td>
      <td>0001-01-01T00:00:00</td>
      <td>15:02:01</td>
    </tr>
    <tr>
      <th>4</th>
      <td>58514988269776425</td>
      <td>IRTKGANJ0004</td>
      <td>گنج</td>
      <td>صندوق س. طلا كيميا زرين كاردان</td>
      <td>39350.0</td>
      <td>39521.0</td>
      <td>39700.0</td>
      <td>350.0</td>
      <td>39474.0</td>
      <td>39400.0</td>
      <td>...</td>
      <td>1272</td>
      <td>3</td>
      <td>13208137.0</td>
      <td>895166.0</td>
      <td>623</td>
      <td>6</td>
      <td>9837925.0</td>
      <td>4265378.0</td>
      <td>0001-01-01T00:00:00</td>
      <td>15:02:01</td>
    </tr>
    <tr>
      <th>5</th>
      <td>28374437855144739</td>
      <td>IRTKALTN0005</td>
      <td>آلتون</td>
      <td>صندوق س.پشتوانه طلاآسمان آلتون</td>
      <td>14771.0</td>
      <td>14828.0</td>
      <td>14875.0</td>
      <td>104.0</td>
      <td>14800.0</td>
      <td>14778.0</td>
      <td>...</td>
      <td>1063</td>
      <td>6</td>
      <td>21870369.0</td>
      <td>3533891.0</td>
      <td>504</td>
      <td>4</td>
      <td>17281950.0</td>
      <td>8122310.0</td>
      <td>0001-01-01T00:00:00</td>
      <td>15:02:01</td>
    </tr>
    <tr>
      <th>6</th>
      <td>38544104313215500</td>
      <td>IRTKJAVA0000</td>
      <td>جواهر</td>
      <td>صندوق س.پشتوانه طلا دناي زاگرس</td>
      <td>16931.0</td>
      <td>16991.0</td>
      <td>17048.0</td>
      <td>117.0</td>
      <td>17000.0</td>
      <td>16930.0</td>
      <td>...</td>
      <td>749</td>
      <td>3</td>
      <td>18477016.0</td>
      <td>2681765.0</td>
      <td>345</td>
      <td>7</td>
      <td>11369591.0</td>
      <td>9789190.0</td>
      <td>0001-01-01T00:00:00</td>
      <td>15:02:01</td>
    </tr>
    <tr>
      <th>7</th>
      <td>30582275818828857</td>
      <td>IRTKNAAB0008</td>
      <td>ناب</td>
      <td>صندوق س.پشتوانه طلا نهايت نگر</td>
      <td>15290.0</td>
      <td>15343.0</td>
      <td>15404.0</td>
      <td>114.0</td>
      <td>15340.0</td>
      <td>15310.0</td>
      <td>...</td>
      <td>894</td>
      <td>5</td>
      <td>13441170.0</td>
      <td>1952669.0</td>
      <td>327</td>
      <td>3</td>
      <td>14023839.0</td>
      <td>1370000.0</td>
      <td>0001-01-01T00:00:00</td>
      <td>15:02:01</td>
    </tr>
    <tr>
      <th>8</th>
      <td>12913156843322499</td>
      <td>IRTKNAHL0009</td>
      <td>نهال</td>
      <td>صندوق س. طلاي سرخ نوويرا</td>
      <td>29999.0</td>
      <td>29935.0</td>
      <td>30264.0</td>
      <td>265.0</td>
      <td>30287.0</td>
      <td>29872.0</td>
      <td>...</td>
      <td>601</td>
      <td>5</td>
      <td>3464104.0</td>
      <td>6025238.0</td>
      <td>361</td>
      <td>2</td>
      <td>3104910.0</td>
      <td>6384432.0</td>
      <td>0001-01-01T00:00:00</td>
      <td>15:02:01</td>
    </tr>
    <tr>
      <th>9</th>
      <td>33144542989832366</td>
      <td>IRTKZFAM0006</td>
      <td>زرفام</td>
      <td>صندوق س.پشتوانه طلا زرفام آشنا</td>
      <td>33967.0</td>
      <td>34084.0</td>
      <td>34176.0</td>
      <td>209.0</td>
      <td>34400.0</td>
      <td>34000.0</td>
      <td>...</td>
      <td>458</td>
      <td>0</td>
      <td>4896818.0</td>
      <td>0.0</td>
      <td>181</td>
      <td>4</td>
      <td>3870750.0</td>
      <td>1026068.0</td>
      <td>0001-01-01T00:00:00</td>
      <td>15:02:01</td>
    </tr>
    <tr>
      <th>10</th>
      <td>51200575796028449</td>
      <td>IRTKSAHR0008</td>
      <td>سحرخيز</td>
      <td>صندوق س. گروه زعفران سحرخيز</td>
      <td>37598.0</td>
      <td>37695.0</td>
      <td>37928.0</td>
      <td>330.0</td>
      <td>37999.0</td>
      <td>37500.0</td>
      <td>...</td>
      <td>496</td>
      <td>0</td>
      <td>1635301.0</td>
      <td>0.0</td>
      <td>195</td>
      <td>2</td>
      <td>1228186.0</td>
      <td>407115.0</td>
      <td>0001-01-01T00:00:00</td>
      <td>15:02:01</td>
    </tr>
    <tr>
      <th>11</th>
      <td>9089296888187061</td>
      <td>IRTKTABA0002</td>
      <td>تابش</td>
      <td>صندوق س.پشتوانه طلا تابان تمدن</td>
      <td>18032.0</td>
      <td>18075.0</td>
      <td>18137.0</td>
      <td>105.0</td>
      <td>18049.0</td>
      <td>18010.0</td>
      <td>...</td>
      <td>414</td>
      <td>2</td>
      <td>7609882.0</td>
      <td>630109.0</td>
      <td>216</td>
      <td>3</td>
      <td>7536074.0</td>
      <td>703917.0</td>
      <td>0001-01-01T00:00:00</td>
      <td>15:02:01</td>
    </tr>
    <tr>
      <th>12</th>
      <td>12390706505809150</td>
      <td>IRTKKIAN0009</td>
      <td>گوهر</td>
      <td>صندوق سكه طلاي كيان</td>
      <td>221800.0</td>
      <td>222655.0</td>
      <td>223300.0</td>
      <td>1500.0</td>
      <td>222283.0</td>
      <td>222083.0</td>
      <td>...</td>
      <td>552</td>
      <td>2</td>
      <td>630365.0</td>
      <td>282350.0</td>
      <td>286</td>
      <td>0</td>
      <td>912715.0</td>
      <td>0.0</td>
      <td>0001-01-01T00:00:00</td>
      <td>15:02:01</td>
    </tr>
    <tr>
      <th>13</th>
      <td>33254899395816171</td>
      <td>IRTKZARF0001</td>
      <td>زر</td>
      <td>صندوق س.پشتوانه طلاي زرافشان</td>
      <td>209430.0</td>
      <td>210141.0</td>
      <td>210320.0</td>
      <td>890.0</td>
      <td>209700.0</td>
      <td>209700.0</td>
      <td>...</td>
      <td>431</td>
      <td>1</td>
      <td>467780.0</td>
      <td>474.0</td>
      <td>236</td>
      <td>2</td>
      <td>256562.0</td>
      <td>211692.0</td>
      <td>0001-01-01T00:00:00</td>
      <td>15:02:01</td>
    </tr>
    <tr>
      <th>14</th>
      <td>4626686276232042</td>
      <td>IRTKNAFS0004</td>
      <td>نفيس</td>
      <td>صندوق س.پشتوانه طلاي صبا</td>
      <td>26458.0</td>
      <td>26685.0</td>
      <td>26810.0</td>
      <td>352.0</td>
      <td>26810.0</td>
      <td>26602.0</td>
      <td>...</td>
      <td>118</td>
      <td>0</td>
      <td>513637.0</td>
      <td>0.0</td>
      <td>87</td>
      <td>0</td>
      <td>513637.0</td>
      <td>0.0</td>
      <td>0001-01-01T00:00:00</td>
      <td>15:02:01</td>
    </tr>
    <tr>
      <th>15</th>
      <td>43531447361624437</td>
      <td>IRTKMOFD0006</td>
      <td>عيار2</td>
      <td>صندوق طلاي عيار مفيد</td>
      <td>123298.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>-123297.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>0</td>
      <td>1</td>
      <td>0.0</td>
      <td>8063151.0</td>
      <td>0</td>
      <td>1</td>
      <td>0.0</td>
      <td>8063151.0</td>
      <td>0001-01-01T00:00:00</td>
      <td>None</td>
    </tr>
    <tr>
      <th>16</th>
      <td>63178324356467930</td>
      <td>IRTKALTN0005</td>
      <td>آلتون2</td>
      <td>صندوق س.پشتوانه طلاآسمان آلتون</td>
      <td>14771.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>-14770.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>0</td>
      <td>1</td>
      <td>0.0</td>
      <td>5900000.0</td>
      <td>0</td>
      <td>1</td>
      <td>0.0</td>
      <td>5900000.0</td>
      <td>0001-01-01T00:00:00</td>
      <td>None</td>
    </tr>
    <tr>
      <th>17</th>
      <td>9838250969540286</td>
      <td>IRTKGANJ0004</td>
      <td>گنج2</td>
      <td>صندوق س. طلا كيميا زرين كاردان</td>
      <td>39350.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>-39349.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>0</td>
      <td>1</td>
      <td>0.0</td>
      <td>5293670.0</td>
      <td>0</td>
      <td>1</td>
      <td>0.0</td>
      <td>5293670.0</td>
      <td>0001-01-01T00:00:00</td>
      <td>None</td>
    </tr>
    <tr>
      <th>18</th>
      <td>68285083509815728</td>
      <td>IRTKLOTF0009</td>
      <td>طلا2</td>
      <td>صندوق س.پشتوانه طلاي لوتوس</td>
      <td>326048.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>-326047.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>0</td>
      <td>1</td>
      <td>0.0</td>
      <td>900000.0</td>
      <td>0</td>
      <td>1</td>
      <td>0.0</td>
      <td>900000.0</td>
      <td>0001-01-01T00:00:00</td>
      <td>12:02:21</td>
    </tr>
    <tr>
      <th>19</th>
      <td>16417568146230314</td>
      <td>IRTKNAHL0009</td>
      <td>نهال2</td>
      <td>صندوق س. طلاي سرخ نوويرا</td>
      <td>29999.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>-29998.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>0</td>
      <td>1</td>
      <td>0.0</td>
      <td>5000000.0</td>
      <td>0</td>
      <td>1</td>
      <td>0.0</td>
      <td>5000000.0</td>
      <td>0001-01-01T00:00:00</td>
      <td>14:21:20</td>
    </tr>
    <tr>
      <th>20</th>
      <td>24634634008171593</td>
      <td>IRTKJAVA0000</td>
      <td>جواهر2</td>
      <td>صندوق س.پشتوانه طلا دناي زاگرس</td>
      <td>16931.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>-16930.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>0</td>
      <td>1</td>
      <td>0.0</td>
      <td>200000.0</td>
      <td>0</td>
      <td>1</td>
      <td>0.0</td>
      <td>200000.0</td>
      <td>0001-01-01T00:00:00</td>
      <td>14:53:22</td>
    </tr>
    <tr>
      <th>21</th>
      <td>10809373624603744</td>
      <td>IRTKSAHR0008</td>
      <td>سحرخيز2</td>
      <td>صندوق س. گروه زعفران سحرخيز</td>
      <td>37598.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>-37597.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>0</td>
      <td>1</td>
      <td>0.0</td>
      <td>200000.0</td>
      <td>0</td>
      <td>1</td>
      <td>0.0</td>
      <td>200000.0</td>
      <td>0001-01-01T00:00:00</td>
      <td>14:16:31</td>
    </tr>
  </tbody>
</table>
<p>22 rows × 56 columns</p>
</div>


    
    
    
    updateSalafMarketsInfo
    


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>Code</th>
      <th>Symbol</th>
      <th>Name</th>
      <th>YesterdayPrice</th>
      <th>FinalPrice</th>
      <th>LastPrice</th>
      <th>PriceChange</th>
      <th>FirstPrice</th>
      <th>MinPrice</th>
      <th>...</th>
      <th>Buy_CountI</th>
      <th>Buy_CountN</th>
      <th>Buy_I_Volume</th>
      <th>Buy_N_Volume</th>
      <th>Sell_CountI</th>
      <th>Sell_CountN</th>
      <th>Sell_I_Volume</th>
      <th>Sell_N_Volume</th>
      <th>ModifyDate</th>
      <th>ModifyTime</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>19104522789503154</td>
      <td>IRBKMLG20483</td>
      <td>عدرپاد2</td>
      <td>سلف ميلگرد درپاد تبريز</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0001-01-01T00:00:00</td>
      <td>13:50:54</td>
    </tr>
    <tr>
      <th>1</th>
      <td>39587043114049835</td>
      <td>IRBKKAL30455</td>
      <td>عكاله3</td>
      <td>سلف شير فرادما كاله</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0001-01-01T00:00:00</td>
      <td>13:48:21</td>
    </tr>
    <tr>
      <th>2</th>
      <td>50941758215965307</td>
      <td>IRBKKAL10457</td>
      <td>عكاله1</td>
      <td>سلف شيرفرادما سوليكو كاله</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0001-01-01T00:00:00</td>
      <td>13:48:21</td>
    </tr>
    <tr>
      <th>3</th>
      <td>279046774105580</td>
      <td>IRBKLAL104C5</td>
      <td>علاله1</td>
      <td>سلف موازي پلي اتيلن سبك فيلم</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0001-01-01T00:00:00</td>
      <td>13:46:41</td>
    </tr>
    <tr>
      <th>4</th>
      <td>13191051508594726</td>
      <td>IRBKSNG504A5</td>
      <td>عسنگ5</td>
      <td>سلف موازي استاندارد آهن مركزي</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0001-01-01T00:00:00</td>
      <td>10:41:35</td>
    </tr>
    <tr>
      <th>5</th>
      <td>30180206509447855</td>
      <td>IRBKBTRY0518</td>
      <td>عباتري</td>
      <td>سلف موازي باتري55 آمپر كرمان</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0001-01-01T00:00:00</td>
      <td>09:22:45</td>
    </tr>
    <tr>
      <th>6</th>
      <td>37997914552081987</td>
      <td>IRBKKER204B6</td>
      <td>عكرمان2</td>
      <td>خودرو كي ام سي كرمان موتور</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0001-01-01T00:00:00</td>
      <td>09:20:10</td>
    </tr>
    <tr>
      <th>7</th>
      <td>23831478970549876</td>
      <td>IRBKAKV10464</td>
      <td>عكيوي1</td>
      <td>سلف استاندارد كيوي روماك گستر</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0001-01-01T00:00:00</td>
      <td>09:11:26</td>
    </tr>
    <tr>
      <th>8</th>
      <td>23953330328814336</td>
      <td>IRBKAKV20463</td>
      <td>عكيوي2</td>
      <td>سلف موازي كيوي روماك گستر</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0001-01-01T00:00:00</td>
      <td>08:47:34</td>
    </tr>
    <tr>
      <th>9</th>
      <td>4139588689414043</td>
      <td>IRBKSNG204A2</td>
      <td>عسنگ2</td>
      <td>سلف سنگ آهن مركزي</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0001-01-01T00:00:00</td>
      <td>08:47:34</td>
    </tr>
    <tr>
      <th>10</th>
      <td>6366366216425323</td>
      <td>IRBKSAEB0579</td>
      <td>عصائب</td>
      <td>سلف موازي ميلگرد صائب تبريز</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0001-01-01T00:00:00</td>
      <td>08:46:24</td>
    </tr>
    <tr>
      <th>11</th>
      <td>71665335194832281</td>
      <td>IRBKAE900385</td>
      <td>عشادگان</td>
      <td>سلف آهن اسفنجي فولاد شادگان</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0001-01-01T00:00:00</td>
      <td>13:49:12</td>
    </tr>
    <tr>
      <th>12</th>
      <td>1185549032856396</td>
      <td>IRBKABAH03B0</td>
      <td>عبهمن</td>
      <td>سلف خودرووانت كارا تك كابين</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0001-01-01T00:00:00</td>
      <td>08:46:24</td>
    </tr>
    <tr>
      <th>13</th>
      <td>63624670675689374</td>
      <td>IRBKSNG304A0</td>
      <td>عسنگ3</td>
      <td>سلف استاندارد سنگ آهن مركزي</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0001-01-01T00:00:00</td>
      <td>08:35:10</td>
    </tr>
    <tr>
      <th>14</th>
      <td>37160087667638961</td>
      <td>IRBKSNG604A3</td>
      <td>عسنگ6</td>
      <td>سلف موازي استاندارد سنگ آهن</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0001-01-01T00:00:00</td>
      <td>08:35:10</td>
    </tr>
    <tr>
      <th>15</th>
      <td>68881802812375814</td>
      <td>IRBKLAL204C3</td>
      <td>علاله2</td>
      <td>سلف پلي اتيلن سبك فيلم</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0001-01-01T00:00:00</td>
      <td>08:35:10</td>
    </tr>
    <tr>
      <th>16</th>
      <td>29651479009942826</td>
      <td>IRBKMILG0482</td>
      <td>عدرپاد1</td>
      <td>سلف موازي ميلگرد درپاد تبريز</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0001-01-01T00:00:00</td>
      <td>08:35:10</td>
    </tr>
    <tr>
      <th>17</th>
      <td>29913990095177623</td>
      <td>IRBKAE2803B2</td>
      <td>عميلگرد2</td>
      <td>سلف ميلگرد آتيه خاورميانه2</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0001-01-01T00:00:00</td>
      <td>08:46:24</td>
    </tr>
    <tr>
      <th>18</th>
      <td>17364413299872861</td>
      <td>IRBKAE840466</td>
      <td>عميلگرد3</td>
      <td>سلف ميلگرد آتيه خاورميانه3</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0001-01-01T00:00:00</td>
      <td>08:35:10</td>
    </tr>
    <tr>
      <th>19</th>
      <td>7431626988889223</td>
      <td>IRBKSEKE0004</td>
      <td>سكه مركزي</td>
      <td>سلف تمام سكه 001 مركزي</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0001-01-01T00:00:00</td>
      <td>08:35:10</td>
    </tr>
    <tr>
      <th>20</th>
      <td>11410725390226728</td>
      <td>IRBKAA001105</td>
      <td>عميلگرد</td>
      <td>سلف ميلگرد آتيه خاورميانه</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0001-01-01T00:00:00</td>
      <td>08:35:10</td>
    </tr>
    <tr>
      <th>21</th>
      <td>28119534882897713</td>
      <td>IRBKKER104B8</td>
      <td>عكرمان1</td>
      <td>سلف كي ام سي كرمان موتور</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0001-01-01T00:00:00</td>
      <td>08:46:24</td>
    </tr>
    <tr>
      <th>22</th>
      <td>45317029711987439</td>
      <td>IRBKSNG104A4</td>
      <td>عسنگ1</td>
      <td>سلف موازي سنگ آهن مركزي</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0001-01-01T00:00:00</td>
      <td>08:35:10</td>
    </tr>
  </tbody>
</table>
<p>23 rows × 56 columns</p>
</div>


    
    
    
    updateCDCMarketsInfo
    


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ContractID</th>
      <th>ContractCode</th>
      <th>ContractDescription</th>
      <th>LastTradingPersianDate</th>
      <th>ContractSize</th>
      <th>ContractSizeUnitFaDesc</th>
      <th>TotalAssetChangesColor</th>
      <th>ContractCurrencyFaDesc</th>
      <th>LastSettlementPrice</th>
      <th>AskPrice1</th>
      <th>...</th>
      <th>OrdersPersianDateTime</th>
      <th>OrdersDateTime</th>
      <th>OrdersCounter</th>
      <th>CommodityID</th>
      <th>CommodityName</th>
      <th>CommodityColor</th>
      <th>CommodityColor1</th>
      <th>TradesCounter</th>
      <th>IsOrdersHighLight</th>
      <th>IsTradesHighLight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>42</td>
      <td>CD1GOC0001</td>
      <td>گواهی سپرده پیوسته تمام سکه بهار آزادی طرح جدید</td>
      <td>1410/12/01</td>
      <td>1.0</td>
      <td>ضریب تبدیل نماد به گروه انبار</td>
      <td>Red</td>
      <td>ریال</td>
      <td>496095158.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>16:47:05</td>
      <td>2024-11-18T16:47:05.3</td>
      <td>-1</td>
      <td>4</td>
      <td>سکه طلا</td>
      <td>#FFD700</td>
      <td>#FFD700</td>
      <td>-1</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>41</td>
      <td>CD1GOB0001</td>
      <td>گواهی سپرده پیوسته شمش طلای +995</td>
      <td>1410/12/01</td>
      <td>10.0</td>
      <td>ضریب تبدیل نماد به گروه انبار</td>
      <td>Red</td>
      <td>ریال</td>
      <td>5773016.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>16:59:51</td>
      <td>2024-11-18T16:59:51.653</td>
      <td>-1</td>
      <td>2</td>
      <td>شمش طلا</td>
      <td>#fdf5e6</td>
      <td>#fdf5e6</td>
      <td>-1</td>
      <td>False</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
<p>2 rows × 69 columns</p>
</div>


    
    
    
    updateAllMarketData
    {'id': 1, 'Description': 'تابلو آتی', 'TradeCount': 4351, 'Buyers': 348, 'Sellers': 362, 'LegalBuyerCount': 6, 'NaturalBuyerCount': 342, 'LegalSellerCount': 3, 'NaturalSellerCount': 359}
    
    updateFutureDateTime
    None
    
    updateFutureMarketsInfo
    


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ContractID</th>
      <th>LastTradingDate</th>
      <th>ContractCode</th>
      <th>ContractDescription</th>
      <th>ContractSize</th>
      <th>ContractSizeUnitFaDesc</th>
      <th>ContractSizeUnitEnDesc</th>
      <th>ContractCurrencyFaDesc</th>
      <th>ContractCurrencyEnDesc</th>
      <th>ContractCurrencyDecimalPlaces</th>
      <th>...</th>
      <th>LegalBuyerCount</th>
      <th>LegalSellerCount</th>
      <th>NaturalBuyerCount</th>
      <th>NaturalSellerCount</th>
      <th>TodayLiveSettlement</th>
      <th>TradeCount</th>
      <th>TradeVolume</th>
      <th>PersianOrdersDateTime</th>
      <th>PersianLastSettlementPriceDate</th>
      <th>PesrsianLastTradingDate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>276</td>
      <td>2024-11-18T00:00:00</td>
      <td>SAFAB03</td>
      <td>قرارداد آتی زعفران نگین تحویل آبان ماه 1403</td>
      <td>100.0</td>
      <td>گرم</td>
      <td>-</td>
      <td>ریال</td>
      <td>Rials</td>
      <td>None</td>
      <td>...</td>
      <td>1</td>
      <td>1</td>
      <td>71</td>
      <td>78</td>
      <td>7.926884e+05</td>
      <td>915</td>
      <td>7304</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>1</th>
      <td>278</td>
      <td>2025-01-08T00:00:00</td>
      <td>ETCDY03</td>
      <td>قرارداد آتی صندوق طلای لوتوس تحویل دی ماه 1403</td>
      <td>1000.0</td>
      <td>واحد</td>
      <td>-</td>
      <td>ریال</td>
      <td>Rials</td>
      <td>None</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>11</td>
      <td>10</td>
      <td>3.448938e+05</td>
      <td>50</td>
      <td>53</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>2</th>
      <td>280</td>
      <td>2024-11-20T00:00:00</td>
      <td>GB30AB03</td>
      <td>قرارداد آتی شمش طلای خام 995 تحویل آبان ماه 1403</td>
      <td>1.0</td>
      <td>گرم</td>
      <td>-</td>
      <td>ریال</td>
      <td>Rials</td>
      <td>None</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>16</td>
      <td>16</td>
      <td>5.751780e+07</td>
      <td>74</td>
      <td>273</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>3</th>
      <td>283</td>
      <td>2024-12-10T00:00:00</td>
      <td>KBAZ03</td>
      <td>قرارداد آتی صندوق طلای کهربا تحویل آذر ماه 1403</td>
      <td>1000.0</td>
      <td>واحد</td>
      <td>-</td>
      <td>ریال</td>
      <td>Rials</td>
      <td>None</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>16</td>
      <td>18</td>
      <td>4.419241e+04</td>
      <td>122</td>
      <td>318</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>4</th>
      <td>284</td>
      <td>2025-04-15T00:00:00</td>
      <td>ETCFA04</td>
      <td>قرارداد آتی صندوق طلای لوتوس تحویل فروردین ماه...</td>
      <td>1000.0</td>
      <td>واحد</td>
      <td>-</td>
      <td>ریال</td>
      <td>Rials</td>
      <td>None</td>
      <td>...</td>
      <td>1</td>
      <td>0</td>
      <td>15</td>
      <td>12</td>
      <td>3.791889e+05</td>
      <td>37</td>
      <td>44</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>5</th>
      <td>285</td>
      <td>2025-03-02T00:00:00</td>
      <td>KBES03</td>
      <td>قرارداد آتی صندوق طلای کهربا تحویل اسفند ماه 1...</td>
      <td>1000.0</td>
      <td>واحد</td>
      <td>-</td>
      <td>ریال</td>
      <td>Rials</td>
      <td>None</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>18</td>
      <td>18</td>
      <td>4.642957e+04</td>
      <td>83</td>
      <td>153</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>6</th>
      <td>288</td>
      <td>2024-12-25T00:00:00</td>
      <td>SAFDY03</td>
      <td>قرارداد آتی زعفران نگین تحویل دی ماه 1403</td>
      <td>100.0</td>
      <td>گرم</td>
      <td>-</td>
      <td>ریال</td>
      <td>Rials</td>
      <td>None</td>
      <td>...</td>
      <td>2</td>
      <td>0</td>
      <td>74</td>
      <td>116</td>
      <td>8.392870e+05</td>
      <td>1050</td>
      <td>5044</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>7</th>
      <td>289</td>
      <td>2025-02-17T00:00:00</td>
      <td>GB29BA03</td>
      <td>قرارداد آتی شمش طلای خام 995 تحویل بهمن ماه 1403</td>
      <td>1.0</td>
      <td>گرم</td>
      <td>-</td>
      <td>ریال</td>
      <td>Rials</td>
      <td>None</td>
      <td>...</td>
      <td>1</td>
      <td>0</td>
      <td>26</td>
      <td>15</td>
      <td>6.302132e+07</td>
      <td>87</td>
      <td>176</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>8</th>
      <td>290</td>
      <td>2025-06-17T00:00:00</td>
      <td>KBKH04</td>
      <td>قرارداد آتی صندوق طلای کهربا تحویل خرداد ماه 1...</td>
      <td>1000.0</td>
      <td>واحد</td>
      <td>-</td>
      <td>ریال</td>
      <td>Rials</td>
      <td>None</td>
      <td>...</td>
      <td>1</td>
      <td>1</td>
      <td>24</td>
      <td>16</td>
      <td>5.075651e+04</td>
      <td>114</td>
      <td>248</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>9</th>
      <td>291</td>
      <td>2025-07-15T00:00:00</td>
      <td>ETCTR04</td>
      <td>قرارداد آتی صندوق طلای لوتوس تحویل تیر ماه 1404</td>
      <td>1000.0</td>
      <td>واحد</td>
      <td>-</td>
      <td>ریال</td>
      <td>Rials</td>
      <td>None</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>7</td>
      <td>7</td>
      <td>4.131200e+05</td>
      <td>21</td>
      <td>24</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>10</th>
      <td>292</td>
      <td>2025-09-16T00:00:00</td>
      <td>KBSH04</td>
      <td>قرارداد آتی صندوق طلای کهربا تحویل شهریور ماه ...</td>
      <td>1000.0</td>
      <td>واحد</td>
      <td>-</td>
      <td>ریال</td>
      <td>Rials</td>
      <td>None</td>
      <td>...</td>
      <td>1</td>
      <td>1</td>
      <td>35</td>
      <td>29</td>
      <td>5.519215e+04</td>
      <td>149</td>
      <td>318</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>11</th>
      <td>293</td>
      <td>2025-03-04T00:00:00</td>
      <td>SAFES03</td>
      <td>قرارداد آتی زعفران نگین تحویل اسفند ماه 1403</td>
      <td>100.0</td>
      <td>گرم</td>
      <td>-</td>
      <td>ریال</td>
      <td>Rials</td>
      <td>None</td>
      <td>...</td>
      <td>1</td>
      <td>0</td>
      <td>95</td>
      <td>121</td>
      <td>9.212390e+05</td>
      <td>751</td>
      <td>3316</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>12</th>
      <td>294</td>
      <td>2025-05-21T00:00:00</td>
      <td>GB31OR04</td>
      <td>قرارداد آتی شمش طلای خام 995 تحویل اردیبهشت ما...</td>
      <td>1.0</td>
      <td>گرم</td>
      <td>-</td>
      <td>ریال</td>
      <td>Rials</td>
      <td>None</td>
      <td>...</td>
      <td>0</td>
      <td>1</td>
      <td>27</td>
      <td>21</td>
      <td>7.102353e+07</td>
      <td>150</td>
      <td>271</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>13</th>
      <td>295</td>
      <td>2025-10-14T00:00:00</td>
      <td>ETCME04</td>
      <td>قرارداد آتی صندوق طلای لوتوس تحویل مهر ماه 1404</td>
      <td>1000.0</td>
      <td>واحد</td>
      <td>-</td>
      <td>ریال</td>
      <td>Rials</td>
      <td>None</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>43</td>
      <td>44</td>
      <td>4.530673e+05</td>
      <td>121</td>
      <td>173</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>14</th>
      <td>296</td>
      <td>2025-05-19T00:00:00</td>
      <td>SAFOR04</td>
      <td>قرارداد آتی زعفران نگین تحویل اردیبهشت ماه 1404</td>
      <td>100.0</td>
      <td>گرم</td>
      <td>-</td>
      <td>ریال</td>
      <td>Rials</td>
      <td>None</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>71</td>
      <td>97</td>
      <td>9.520028e+05</td>
      <td>627</td>
      <td>2543</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
<p>15 rows × 75 columns</p>
</div>


    
    
    
    updateMarketsInfo
    


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>_StrikeLevel</th>
      <th>_StrikePrice</th>
      <th>_LastUpdate</th>
      <th>_PutContractVisibility</th>
      <th>_ContractCategory</th>
      <th>_CommodityGroup</th>
      <th>_ContractSubGroup</th>
      <th>_CallContractID</th>
      <th>_CallContractCode</th>
      <th>_CallContractDescription</th>
      <th>...</th>
      <th>PutTradesVolume</th>
      <th>PutTradesVolumeVisibility</th>
      <th>PutTradesValue</th>
      <th>PutTradesValueCurrencyFaDesc</th>
      <th>PutTradesValueCurrencyEnDesc</th>
      <th>PutOpenInterests</th>
      <th>PutOpenInterestsChanges</th>
      <th>PutOpenInterestsChangesPercent</th>
      <th>PutOpenInterestsChangesVisibility</th>
      <th>PutOpenInterestsChangesColor</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-1</td>
      <td>300000.0</td>
      <td>2024-11-18T17:00:03.793</td>
      <td>Visible</td>
      <td>DY03\t\t\tتاریخ سررسید: 1403/10/16</td>
      <td>ETCDY03</td>
      <td>ETCDY03</td>
      <td>1001126</td>
      <td>FEDY03C30</td>
      <td>قرارداد اختیار معامله خرید مبتنی بر قرارداد آت...</td>
      <td>...</td>
      <td>NaN</td>
      <td>Collapsed</td>
      <td>NaN</td>
      <td></td>
      <td></td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>Collapsed</td>
      <td>Gray</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>330000.0</td>
      <td>2024-11-18T17:00:03.79</td>
      <td>Visible</td>
      <td>DY03\t\t\tتاریخ سررسید: 1403/10/16</td>
      <td>ETCDY03</td>
      <td>ETCDY03</td>
      <td>1001127</td>
      <td>FEDY03C33</td>
      <td>قرارداد اختیار معامله خرید مبتنی بر قرارداد آت...</td>
      <td>...</td>
      <td>NaN</td>
      <td>Collapsed</td>
      <td>NaN</td>
      <td></td>
      <td></td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>Collapsed</td>
      <td>Gray</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>360000.0</td>
      <td>2024-11-18T17:00:03.79</td>
      <td>Visible</td>
      <td>DY03\t\t\tتاریخ سررسید: 1403/10/16</td>
      <td>ETCDY03</td>
      <td>ETCDY03</td>
      <td>1001128</td>
      <td>FEDY03C36</td>
      <td>قرارداد اختیار معامله خرید مبتنی بر قرارداد آت...</td>
      <td>...</td>
      <td>NaN</td>
      <td>Collapsed</td>
      <td>NaN</td>
      <td></td>
      <td></td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>Collapsed</td>
      <td>Gray</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-1</td>
      <td>4600000.0</td>
      <td>2024-11-18T17:00:03.797</td>
      <td>Visible</td>
      <td>BA03\t\t\tتاریخ سررسید: 1403/11/27</td>
      <td>CDC</td>
      <td>CDCBA03</td>
      <td>1001150</td>
      <td>GBBA03C460</td>
      <td>قرارداد اختیار معامله خرید شمش طلا سررسید بهمن...</td>
      <td>...</td>
      <td>NaN</td>
      <td>Collapsed</td>
      <td>NaN</td>
      <td></td>
      <td></td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>Collapsed</td>
      <td>Gray</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0</td>
      <td>4800000.0</td>
      <td>2024-11-18T17:00:03.797</td>
      <td>Visible</td>
      <td>BA03\t\t\tتاریخ سررسید: 1403/11/27</td>
      <td>CDC</td>
      <td>CDCBA03</td>
      <td>1001152</td>
      <td>GBBA03C480</td>
      <td>قرارداد اختیار معامله خرید شمش طلا سررسید بهمن...</td>
      <td>...</td>
      <td>NaN</td>
      <td>Collapsed</td>
      <td>NaN</td>
      <td></td>
      <td></td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>Collapsed</td>
      <td>Gray</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>82</th>
      <td>-1</td>
      <td>330000.0</td>
      <td>2024-11-18T17:00:03.863</td>
      <td>Visible</td>
      <td>TR04\t\t\tتاریخ سررسید: 1404/04/29</td>
      <td>LG ETC</td>
      <td>LG ETCTR04</td>
      <td>1001277</td>
      <td>TLTR04C33</td>
      <td>قرارداد اختیار معامله خرید واحدهای سرمایه گذار...</td>
      <td>...</td>
      <td>NaN</td>
      <td>Collapsed</td>
      <td>NaN</td>
      <td></td>
      <td></td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>Collapsed</td>
      <td>Gray</td>
    </tr>
    <tr>
      <th>83</th>
      <td>0</td>
      <td>350000.0</td>
      <td>2024-11-18T17:00:03.863</td>
      <td>Visible</td>
      <td>TR04\t\t\tتاریخ سررسید: 1404/04/29</td>
      <td>LG ETC</td>
      <td>LG ETCTR04</td>
      <td>1001278</td>
      <td>TLTR04C35</td>
      <td>قرارداد اختیار معامله خرید واحدهای سرمایه گذار...</td>
      <td>...</td>
      <td>NaN</td>
      <td>Collapsed</td>
      <td>NaN</td>
      <td></td>
      <td></td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>Collapsed</td>
      <td>Gray</td>
    </tr>
    <tr>
      <th>84</th>
      <td>1</td>
      <td>370000.0</td>
      <td>2024-11-18T17:00:03.867</td>
      <td>Visible</td>
      <td>TR04\t\t\tتاریخ سررسید: 1404/04/29</td>
      <td>LG ETC</td>
      <td>LG ETCTR04</td>
      <td>1001279</td>
      <td>TLTR04C37</td>
      <td>قرارداد اختیار معامله خرید واحدهای سرمایه گذار...</td>
      <td>...</td>
      <td>NaN</td>
      <td>Collapsed</td>
      <td>NaN</td>
      <td></td>
      <td></td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>Collapsed</td>
      <td>Gray</td>
    </tr>
    <tr>
      <th>85</th>
      <td>2</td>
      <td>390000.0</td>
      <td>2024-11-18T17:00:03.867</td>
      <td>Visible</td>
      <td>TR04\t\t\tتاریخ سررسید: 1404/04/29</td>
      <td>LG ETC</td>
      <td>LG ETCTR04</td>
      <td>1001280</td>
      <td>TLTR04C39</td>
      <td>قرارداد اختیار معامله خرید واحدهای سرمایه گذار...</td>
      <td>...</td>
      <td>NaN</td>
      <td>Collapsed</td>
      <td>NaN</td>
      <td></td>
      <td></td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>Collapsed</td>
      <td>Gray</td>
    </tr>
    <tr>
      <th>86</th>
      <td>3</td>
      <td>410000.0</td>
      <td>2024-11-18T17:00:03.867</td>
      <td>Visible</td>
      <td>TR04\t\t\tتاریخ سررسید: 1404/04/29</td>
      <td>LG ETC</td>
      <td>LG ETCTR04</td>
      <td>1001281</td>
      <td>TLTR04C41</td>
      <td>قرارداد اختیار معامله خرید واحدهای سرمایه گذار...</td>
      <td>...</td>
      <td>NaN</td>
      <td>Collapsed</td>
      <td>NaN</td>
      <td></td>
      <td></td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>Collapsed</td>
      <td>Gray</td>
    </tr>
  </tbody>
</table>
<p>87 rows × 302 columns</p>
</div>


    
    
    
    
