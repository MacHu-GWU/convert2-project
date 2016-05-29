#!/usr/bin/env python
# -*- coding: utf-8 -*-

from convert2 import any2date
from convert2.packages.rolex import utc
from convert2.packages.six import PY3
import pytest
import numpy as np
import pandas as pd
from datetime import datetime, date, timedelta


def test_parse_datetime():
    int_ = 1
    float_ = 1.0

    # None
    assert any2date(None) is None
    assert any2date(np.nan) is None

    # int, long, np.int, np.int8, np.int16, np.int32, np.int64
    assert any2date(int_) == date(1, 1, 1)
    assert any2date(np.int(int_)) == date(1, 1, 1)
    assert any2date(np.int8(int_)) == date(1, 1, 1)
    assert any2date(np.int16(int_)) == date(1, 1, 1)
    assert any2date(np.int32(int_)) == date(1, 1, 1)
    assert any2date(np.int64(int_)) == date(1, 1, 1)

    # float, np.float, np.float16, np.float32, np.float64
    with pytest.raises(ValueError) as excinfo:
        any2date(float_)

    # np.datetime64, pd.tslib.Timestamp
    assert any2date(np.datetime64("1970-01-01 00:00:00Z")) == date(1970, 1, 1)
    assert any2date(
        pd.tslib.Timestamp("1970-01-01 00:00:00Z")) == date(1970, 1, 1)
    assert any2date(datetime(1970, 1, 1, 0, 0, 0)) == date(1970, 1, 1)

    # date
    assert any2date(date(1970, 1, 1)) == date(1970, 1, 1)


if __name__ == "__main__":
    import py
    py.test.cmdline.main("--tb=native -s")
