#!/usr/bin/env python
# -*- coding: utf-8 -*-

from zipline.data.bundles import register
from zipline.data.bundles.yahoo_csv import yahoo_csv_equities # yahoo_csv.py need to be placed in zipline.data.bundles

tickers = {
     "SPY", "VXX", "VXZ"
}
register(
    'yahoo_csv_bundle1',
    yahoo_csv_equities(tickers, path='~/csv/'),
)
register(
    'yahoo_csv_bundle2',
    yahoo_csv_equities({}, path='~/csv/'),
)