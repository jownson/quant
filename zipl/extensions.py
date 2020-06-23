import pandas as pd

from zipline.data.bundles import register
from zipline.data.bundles.csvdir import csvdir_equities

start_session = pd.Timestamp('2012-1-3', tz='utc')
end_session = pd.Timestamp('2012-2-28', tz='utc')

register(
    'custom-csvdir-bundle',
    csvdir_equities(
        ['daily'],
        'c:\\quandl',
    ),
    calendar_name='NYSE',  # US equities
    start_session=start_session,
    end_session=end_session
)

# zipline ingest -b custom-csvdir-bundle
# set CSVDIR=/cvsdir
