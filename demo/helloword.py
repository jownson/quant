import os
from os.path import abspath, basename, dirname, exists, isfile
from shutil import move, rmtree
from subprocess import check_call

HERE = dirname(abspath(__file__))
ZIPLINE_ROOT = dirname(HERE)

print(ZIPLINE_ROOT)

