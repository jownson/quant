import pandas as pd
from pandas import DataFrame

in_csv_file = 'C:\\BMS.csv';
bcl_out_file = 'C:\\res.csv';


# 分析BCL数据，需求电压和需求电流
def solve_bcl_data(csv_file):
    bcl = csv_file[csv_file["帧 ID"] == '0x181056F4']
    res = DataFrame(columns=('volt', 'current'))

    i = 0;
    for data in bcl['数据']:
        need_volt = int(data[0:2], 16) + int(data[3:5], 16) * 256;
        need_curr = (int(data[6:8], 16) + int(data[9:11], 16) * 256) - 4000;
        res.loc[i] = [float(need_volt) / 10, float(need_curr) / 10];
        i = i + 1;
    return res;


df = pd.read_csv(in_csv_file, encoding='gb2312')
res = solve_bcl_data(df)
res.to_csv(bcl_out_file, encoding='gb2312');

print("---------------end---------------------")

# print(df.keys());
# print(df.head(5))   #打印前5行
# print('时间标识 列 是: ' + str(df['时间标识'].dtypes))
# print(df['时间标识'][0] + df['时间标识'][1])
# print(need_volt['数据'])

# print(df['序号']+df['时间标识'])
# print(df['帧ID'] + ',' + df['数据(HEX)'])


# print(df[df['帧ID'] == '0x1808f456'])
