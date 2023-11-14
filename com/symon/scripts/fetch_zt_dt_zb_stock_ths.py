import pandas as pd
import csv
from com.symon.crawler.ths import data_api as ths

"""
从同花顺抓取涨停炸板股票
"""


if __name__ == '__main__':
    open_limit_stock_data = ths.get_open_limit_pool_after_date(ths.get_first_trade_day("20231114"), 1)
    df = pd.DataFrame(open_limit_stock_data)
    df.to_csv(f"../crawler/ths/data/2023-涨停炸板股票.csv", encoding='utf-8', header=False, mode='a', index=False, quoting=csv.QUOTE_NONE)