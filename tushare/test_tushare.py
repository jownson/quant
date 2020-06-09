import time
import tushare
import tushare as ts

print(tushare.__version__)

# ts.set_token('c3e325e4b592c23ccda5c725041659db55e87111f245eac3bb7b9dc2')
pro = ts.pro_api('c3e325e4b592c23ccda5c725041659db55e87111f245eac3bb7b9dc2')


# df = pro.trade_cal(exchange='', start_date='20180901', end_date='20181001', fields='exchange,cal_date,is_open,pretrade_date', is_open='0')
# print(df)

# df = pro.query('trade_cal', exchange='', start_date='20180901', end_date='20181001', fields='exchange,cal_date,is_open,pretrade_date', is_open='0')


df = pro.daily(trade_date='20200325')
print(df)

# df = pro.trade_cal(exchange='SSE', is_open='1', start_date='20200101', end_date='20200401', fields='cal_date')
# print(df)

# def get_daily(self, ts_code='', trade_date='', start_date='', end_date=''):
#     for _ in range(3):
#         try:
#             if trade_date:
#                 df = self.pro.daily(ts_code=ts_code, trade_date=trade_date)
#             else:
#                 df = self.pro.daily(ts_code=ts_code, start_date=start_date, end_date=end_date)
#         except:
#             time.sleep(1)
#     else:
#         return df
#
#
# for date in df['cal_date'].values:
#     df = get_daily(date)
#     print(df)
