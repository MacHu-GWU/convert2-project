#!/usr/bin/env python
# -*- coding: utf-8 -*-

from convert2.converter import any2datetime
from convert2.lib.rolex import utc
from convert2.lib.six import PY3
import pytest
import numpy as np
import pandas as pd
from datetime import datetime, date, timedelta


def test_parse_datetime():
    int_ = 1
    float_ = 1.0

    # None
    assert any2datetime(None) is None
    assert any2datetime(np.nan) is None

    # int, long, np.int, np.int8, np.int16, np.int32, np.int64
    assert any2datetime(int_) == datetime(1970, 1, 1, 0, 0, 1)
    assert any2datetime(np.int(int_)) == datetime(1970, 1, 1, 0, 0, 1)
    assert any2datetime(np.int8(int_)) == datetime(1970, 1, 1, 0, 0, 1)
    assert any2datetime(np.int16(int_)) == datetime(1970, 1, 1, 0, 0, 1)
    assert any2datetime(np.int32(int_)) == datetime(1970, 1, 1, 0, 0, 1)
    assert any2datetime(np.int64(int_)) == datetime(1970, 1, 1, 0, 0, 1)

    # float, np.float, np.float16, np.float32, np.float64
    assert any2datetime(float_) == datetime(1970, 1, 1, 0, 0, 1)
    assert any2datetime(np.float(float_)) == datetime(1970, 1, 1, 0, 0, 1)
    assert any2datetime(np.float16(float_)) == datetime(1970, 1, 1, 0, 0, 1)
    assert any2datetime(np.float32(float_)) == datetime(1970, 1, 1, 0, 0, 1)
    assert any2datetime(np.float64(float_)) == datetime(1970, 1, 1, 0, 0, 1)

    # np.datetime64, pd.tslib.Timestamp
    assert any2datetime(
        np.datetime64("1970-01-01 00:00:00Z")) == datetime(1970, 1, 1, 0, 0, 0)
    assert any2datetime(pd.tslib.Timestamp(
        "1970-01-01 00:00:00Z")) == datetime(1970, 1, 1, 0, 0, 0, tzinfo=utc)
    assert any2datetime(datetime(1970, 1, 1, 0, 0, 0)) == datetime(
        1970, 1, 1, 0, 0, 0)

    # date
    assert any2datetime(date(1970, 1, 1)) == datetime(1970, 1, 1, 0, 0, 0)


if __name__ == "__main__":
    import py
    py.test.cmdline.main("--tb=native -s")
