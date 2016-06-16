#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
注意: numpy在1.11.0版本之前, 在创建datetime64对象时, 总是默认时间为local time。
而且输出的时候也是local time。而在1.11.0版本之后, 总是默认时间为utc time, 如果
字符串中有时区信息, 则仍然会正确的得到时区信息, 但无论怎样, 都输出为utc time。
"""

from __future__ import print_function
from datetime import datetime
import numpy as np, pandas as pd

print("numpy's version = %s" % np.__version__)

def test_datetime_naive_or_local():
    dt_str = "2000-01-01 00:00:00"
    dt_np = np.datetime64(dt_str)
    dt_pd = pd.tslib.Timestamp(dt_str)
    
    print(dt_np)
    print(dt_pd)
    print(dt_np.astype(datetime))
    print(dt_pd.to_pydatetime())
    
test_datetime_naive_or_local()