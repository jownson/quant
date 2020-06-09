import time
import tushare
import tushare as ts

pro = ts.pro_api('c3e325e4b592c23ccda5c725041659db55e87111f245eac3bb7b9dc2')

# 一次性获取全部数据
ts.get_hist_data('600848')


print(ts)
