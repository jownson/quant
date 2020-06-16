# 默认数据 需要绑定一次
# 需要 Quandl 的 API key 来获取默认数据 https://docs.quandl.com/docs#section-authentication
# 可以去网站免费注册一个账号（获取API_KEY），并使用如下命令将数据灌入zipline。

$QUANDL_API_KEY = < yourkey > zipline
ingest[-b < bundle >]

# 其中<bundle> 是数据包的名称，默认为 quandl
$QUANDL_API_KEY = jYsYCRqJTk1C6GojWZ3 - zipline
ingest - b
quandl

# 从.csv文件中加载数据
# 导入 csvdir 和 pandas 包 (可以编辑 ~/.zipline/extension.py，也可以直接写在策略中)
import pandas as pd

from zipline.data.bundles import register
from zipline.data.bundles.csvdir import csvdir_equities

# 指定开始和结束时间：
start_session = pd.Timestamp('2016-1-1', tz='utc')
end_session = pd.Timestamp('2018-1-1', tz='utc')
# 然后我们可以传入 .csv 文件路径，用 register() 注册我们的自己编写的 bundle
register(
    'custom-csvdir-bundle',
    csvdir_equities(
        ['daily'],
        '/path/to/your/csvs',
    ),
    calendar_name='NYSE',  # US equities
    start_session=start_session,
    end_session=end_session
)
# 运行命令导入自己编写的 bundle
$zipline
ingest - b
custom - csvdir - bundle

# 我们可以通过命令行传递我们的csvs的位置
$CSVDIR =/path/to/your/csvs
zipline
ingest - b
custom - csvdir - bundle

# 默认情况下，数据将被写在 $ZIPLINE_ROOT/data/<bundle> （默认情况下 ZIPLINE_ROOT=~/.zipline ）
# ingest 会将新数据写入$ZIPLINE_ROOT/data/<bundle> 并以当前日期命名，可以按日期查看旧数据，用旧数据进行回测。 使用旧数据进行回测，可以更容易地重现回测结果
# zipline 默认保存所有绑定的数据 数据目录会非常大，可以使用清理命令
# clean everything older than <date>
$zipline
clean[-b < bundle >] - -before < date >

# clean everything newer than <date>
$zipline
clean[-b < bundle >] - -after < date >

# keep everything in the range of [before, after] and delete the rest
$ zipline
clean[-b < bundle >] - -before < date > --after < after >

# clean all but the last <int> runs
$ zipline
clean[-b < bundle >] - -keep - last
0  # 数字表示保留最近的n次数据

# 查看zipline 数据
$ zipline
bundles