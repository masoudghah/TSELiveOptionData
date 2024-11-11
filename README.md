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
# read_data_from_file = False

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
      <td>16570</td>
      <td>16120</td>
      <td>20240615</td>
      <td>20241120</td>
      <td>20000</td>
      <td>8</td>
      <td>43072367801777779</td>
      <td>...</td>
      <td>19087</td>
      <td>122</td>
      <td>اختيارخ اهرم-20000-1403/08/30</td>
      <td>ضهرم8005</td>
      <td>12</td>
      <td>50</td>
      <td>16</td>
      <td>1249</td>
      <td>246240</td>
      <td>call</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1000</td>
      <td>43443105991896600</td>
      <td>ارزش</td>
      <td>18550</td>
      <td>18110</td>
      <td>20240817</td>
      <td>20241215</td>
      <td>18000</td>
      <td>33</td>
      <td>43060893718114997</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>اختيارخ ارزش-18000-1403/09/25</td>
      <td>ضارش9006</td>
      <td>11</td>
      <td>200</td>
      <td>0</td>
      <td>0</td>
      <td>409</td>
      <td>call</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1000</td>
      <td>44604318643489231</td>
      <td>بيدار</td>
      <td>7870</td>
      <td>7660</td>
      <td>20241009</td>
      <td>20250108</td>
      <td>10000</td>
      <td>57</td>
      <td>40446253344612873</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>اختيارخ بيدار-10000-1403/10/19</td>
      <td>ضبيد1006</td>
      <td>1</td>
      <td>300</td>
      <td>300</td>
      <td>200</td>
      <td>503</td>
      <td>call</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1000</td>
      <td>778253364357513</td>
      <td>وبملت</td>
      <td>2204</td>
      <td>2143</td>
      <td>20240817</td>
      <td>20241218</td>
      <td>1500</td>
      <td>36</td>
      <td>17640843853734260</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>اختيارخ وبملت-1500-1403/09/28</td>
      <td>ضملت9013</td>
      <td>50</td>
      <td>180</td>
      <td>1000</td>
      <td>1000</td>
      <td>43062</td>
      <td>call</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1000</td>
      <td>778253364357513</td>
      <td>وبملت</td>
      <td>2204</td>
      <td>2143</td>
      <td>20240817</td>
      <td>20241218</td>
      <td>1800</td>
      <td>36</td>
      <td>62195326705007487</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>اختيارخ وبملت-1800-1403/09/28</td>
      <td>ضملت9016</td>
      <td>0</td>
      <td>0</td>
      <td>690</td>
      <td>10</td>
      <td>304</td>
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
      <th>1977</th>
      <td>10</td>
      <td>67522512921942106</td>
      <td>پادا</td>
      <td>149245</td>
      <td>149008</td>
      <td>20240707</td>
      <td>20250105</td>
      <td>190000</td>
      <td>54</td>
      <td>40489538509583284</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>اختيارف پادا-190000-14031016</td>
      <td>طپادا1010</td>
      <td>100</td>
      <td>1000</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>put</td>
    </tr>
    <tr>
      <th>1978</th>
      <td>1000</td>
      <td>25211433301660888</td>
      <td>خپارس</td>
      <td>752</td>
      <td>731</td>
      <td>20241015</td>
      <td>20241201</td>
      <td>700</td>
      <td>19</td>
      <td>64999726043881502</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>اختيارف خپارس-700-14030911</td>
      <td>طخپارس902</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>put</td>
    </tr>
    <tr>
      <th>1979</th>
      <td>1000</td>
      <td>25211433301660888</td>
      <td>خپارس</td>
      <td>752</td>
      <td>731</td>
      <td>20241015</td>
      <td>20241201</td>
      <td>800</td>
      <td>19</td>
      <td>66718346568169696</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>اختيارف خپارس-800-14030911</td>
      <td>طخپارس904</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>put</td>
    </tr>
    <tr>
      <th>1980</th>
      <td>1000</td>
      <td>25211433301660888</td>
      <td>خپارس</td>
      <td>752</td>
      <td>731</td>
      <td>20241015</td>
      <td>20250202</td>
      <td>600</td>
      <td>82</td>
      <td>31096670670746865</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>اختيارف خپارس-600-14031114</td>
      <td>طخپارس1100</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>put</td>
    </tr>
    <tr>
      <th>1981</th>
      <td>1000</td>
      <td>53059909885484371</td>
      <td>رويين</td>
      <td>10437</td>
      <td>10371</td>
      <td>20240917</td>
      <td>20250209</td>
      <td>12000</td>
      <td>89</td>
      <td>20606279281243326</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>اختيارف رويين-12000-14031121</td>
      <td>طرويين1106</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>put</td>
    </tr>
  </tbody>
</table>
<p>1982 rows × 26 columns</p>
</div>


    contract_size                                        1000
    ua_tse_code                             17914401175772326
    ua_ticker                                            اهرم
    ua_close_price                                      16570
    ua_yesterday_price                                  16120
    begin_date                                       20240615
    end_date                                         20241120
    strike_price                                        20000
    days_to_maturity                                        8
    tse_code                                43072367801777779
    last_price                                             16
    open_positions                                     246240
    close_price                                            14
    yesterday_price                                        24
    notional_value                             316271590000.0
    trades_value                                  258156000.0
    trades_volume                                       19087
    trades_num                                            122
    name                        اختيارخ اهرم-20000-1403/08/30
    ticker                                           ضهرم8005
    bid_price                                              12
    bid_volume                                             50
    ask_price                                              16
    ask_volume                                           1249
    yesterday_open_positions                           246240
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

    total_trade_value: 287 B Toman
    
    


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
      <td>64.77 B Toman</td>
    </tr>
    <tr>
      <th>1</th>
      <td>ضخود9027</td>
      <td>29.09 B Toman</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ضخود9026</td>
      <td>24.23 B Toman</td>
    </tr>
    <tr>
      <th>3</th>
      <td>ضهرم8003</td>
      <td>20.44 B Toman</td>
    </tr>
    <tr>
      <th>4</th>
      <td>ضهرم9004</td>
      <td>7.51 B Toman</td>
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
      <td>35.83 B Toman</td>
    </tr>
    <tr>
      <th>1</th>
      <td>طخود9027</td>
      <td>13.32 B Toman</td>
    </tr>
    <tr>
      <th>2</th>
      <td>طخود9026</td>
      <td>7.85 B Toman</td>
    </tr>
    <tr>
      <th>3</th>
      <td>طهرم8003</td>
      <td>6.19 B Toman</td>
    </tr>
    <tr>
      <th>4</th>
      <td>طهرم9004</td>
      <td>5.56 B Toman</td>
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
      <td>107.75 B Toman</td>
      <td>56.02 B Toman</td>
      <td>163.77 B Toman</td>
    </tr>
    <tr>
      <th>1</th>
      <td>خودرو</td>
      <td>76.91 B Toman</td>
      <td>22.03 B Toman</td>
      <td>98.95 B Toman</td>
    </tr>
    <tr>
      <th>2</th>
      <td>شستا</td>
      <td>8.33 B Toman</td>
      <td>0.57 B Toman</td>
      <td>8.89 B Toman</td>
    </tr>
    <tr>
      <th>3</th>
      <td>خساپا</td>
      <td>3.31 B Toman</td>
      <td>0.0 B Toman</td>
      <td>3.31 B Toman</td>
    </tr>
    <tr>
      <th>4</th>
      <td>توان</td>
      <td>2.77 B Toman</td>
      <td>0.02 B Toman</td>
      <td>2.78 B Toman</td>
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
      <td>1798.0</td>
      <td>اختیارخ اهرم-16000-1403/11/24</td>
      <td>1626.0</td>
      <td>20</td>
      <td>1980.0</td>
      <td>75</td>
      <td>1</td>
      <td>2</td>
      <td>1800.0</td>
      <td>...</td>
      <td>4.297640e+08</td>
      <td>1403/8/21 12:13</td>
      <td>0</td>
      <td>-272.0</td>
      <td>-13.14</td>
      <td>-419.0</td>
      <td>-20.24</td>
      <td>18154069997422059</td>
      <td>None</td>
      <td>1000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.0</td>
      <td>1305.0</td>
      <td>اختیارخ توان-16000-14031002</td>
      <td>1250.0</td>
      <td>20</td>
      <td>1340.0</td>
      <td>121</td>
      <td>1</td>
      <td>1</td>
      <td>1401.0</td>
      <td>...</td>
      <td>2.764052e+09</td>
      <td>1403/8/21 12:27</td>
      <td>0</td>
      <td>-10.0</td>
      <td>-0.76</td>
      <td>-125.0</td>
      <td>-9.51</td>
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
      <td>0.0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.000000e+00</td>
      <td>1403/8/14 12:26</td>
      <td>0</td>
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
      <td>0.000000e+00</td>
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
      <td>0.000000e+00</td>
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
     'CP12': 0,
     'ClosingPrice': 1798.0,
     'CompanyTitle': 'اختیارخ اهرم-16000-1403/11/24',
     'GroupStateID': 8,
     'HighAllowedPrice': 500000.0,
     'HighPrice': 1950.0,
     'InstrumentCode': '18154069997422059',
     'IsCautionAgreement': False,
     'IsSepahAgreement': False,
     'LastTradedPrice': 1651.0,
     'LotSize': 1,
     'LowAllowedPrice': 1.0,
     'LowPercent': 100,
     'LowPrice': 1600.0,
     'MarketType': 'MarketType.BuyOption',
     'MaxPercent': 24055,
     'MaxQuantityOrder': 1000,
     'MinQuantityOrder': 1,
     'NSCCode': 'IRO9AHRM2501',
     'RefPrice': 2070.0,
     'Symbol': 'ضهرم1105',
     'SymbolStateId': 1,
     'TickSize': 1.0,
     'TotalNumberOfSharesTraded': 239,
     'TotalNumberOfTrades': 13,
     'TotalTradeValue': 429764000.0,
     'TradeDate': '1403/08/21 - 12:13:45',
     'UA_LastTradedPrice': 16460.0,
     'UA_isin': 'IRT1AHRM0001',
     'YesterdayPrice': 2070.0,
     'contractSize': 1000,
     'contractStartDate': '1403/07/01',
     'cpv': -272.0,
     'cpvp': -13.14,
     'crn': 'ریال',
     'crp': 1,
     'exerciseDate': '1403/11/24',
     'gc': '3A',
     'initial_margin': 3320000.0,
     'iso': True,
     'lpv': -419.0,
     'lpvp': -20.24,
     'mbop': 0,
     'mcaop': 112000,
     'mcop': 112000,
     'mmop': 2250000,
     'openPositionNum': 5712,
     'pv': 0.0,
     'rm': 5118000.0,
     'strikePrice': 16000.0,
     'th': 434306.0,
     'tl': 0.0,
     'vs': -1}
    


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
      <td>1626.0</td>
      <td>1980.0</td>
      <td>75</td>
      <td>20</td>
      <td>1</td>
      <td>2</td>
      <td>IRO9AHRM2501</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1625.0</td>
      <td>1990.0</td>
      <td>66</td>
      <td>50</td>
      <td>1</td>
      <td>1</td>
      <td>IRO9AHRM2501</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1602.0</td>
      <td>2060.0</td>
      <td>81</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>IRO9AHRM2501</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1601.0</td>
      <td>2080.0</td>
      <td>16</td>
      <td>20</td>
      <td>1</td>
      <td>1</td>
      <td>IRO9AHRM2501</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1600.0</td>
      <td>2199.0</td>
      <td>10</td>
      <td>15</td>
      <td>1</td>
      <td>1</td>
      <td>IRO9AHRM2501</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>

