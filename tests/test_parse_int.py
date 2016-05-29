#!/usr/bin/env python
# -*- coding: utf-8 -*-


from convert2.converter import any2int
from convert2.lib.rolex import utc
import pytest
import numpy as np
import pandas as pd
from datetime import datetime, date, timedelta


def test_parse_int():
    int_ = 1
    long_ = 2 ** 48

    # None
    assert any2int(None) is None
    assert any2int(np.nan) is None

    # int, long, np.int, np.int8, np.int16, np.int32, np.int64
    assert any2int(int_) == int_
    assert any2int(np.int(int_)) == int_
    assert any2int(np.int8(int_)) == int_
    assert any2int(np.int16(int_)) == int_
    assert any2int(np.int32(int_)) == int_
    assert any2int(np.int64(int_)) == int_
    assert any2int(long_) == long_
    assert any2int(-long_) == -long_
    assert any2int(np.int64(long_)) == long_
    assert any2int(np.int64(-long_)) == -long_

    # float, np.float, np.float16, np.float32, np.float64
    assert any2int(1.001) == int_
    assert any2int(0.999) == int_
    assert any2int(np.float(1.001)) == int_
    assert any2int(np.float(0.999)) == int_
    assert any2int(np.float16(1.001)) == int_
    assert any2int(np.float16(0.999)) == int_
    assert any2int(np.float32(1.001)) == int_
    assert any2int(np.float32(0.999)) == int_
    assert any2int(np.float64(1.001)) == int_
    assert any2int(np.float64(0.999)) == int_

    # str, unicode, np.str
    assert any2int("1") == int_
    assert any2int("1.001") == int_
    assert any2int("0.999") == int_
    assert any2int("a1b") == int_
    assert any2int("a 1.001 b") == int_
    assert any2int("a 0.999 b") == int_

    with pytest.raises(ValueError) as excinfo:
        any2int("a1b2c")

    with pytest.raises(ValueError) as excinfo:
        any2int("a1.1b2.2c")

    assert any2int(u"1") == int_
    assert any2int(u"1.001") == int_
    assert any2int(u"0.999") == int_
    assert any2int(u"a1b") == int_
    assert any2int(u"a 1.001 b") == int_
    assert any2int(u"a 0.999 b") == int_

    assert any2int(np.str("1")) == int_
    assert any2int(np.str("1.001")) == int_
    assert any2int(np.str("0.999")) == int_
    assert any2int(np.str("a1b")) == int_
    assert any2int(np.str("a 1.001 b")) == int_
    assert any2int(np.str("a 0.999 b")) == int_

    any2int.EXTRACT_NUMBER_FROM_TEXT = False
    with pytest.raises(ValueError) as excinfo:
        any2int("a1b")
    any2int.EXTRACT_NUMBER_FROM_TEXT = True

    # datetime, np.datetime64, pd.tslib.Timestamp
    assert any2int(datetime(1970, 1, 1, 0, 0, 1, tzinfo=utc)) == int_
    assert any2int(np.datetime64("1970-01-01 00:00:01Z")) == int_
    assert any2int(pd.tslib.Timestamp("1970-01-01 00:00:01Z")) == int_

    assert isinstance(
        any2int(datetime(1970, 1, 1, 0, 0, 1, tzinfo=utc)), int) is True
    assert isinstance(
        any2int(np.datetime64("1970-01-01 00:00:01Z")), int) is True
    assert isinstance(
        any2int(pd.tslib.Timestamp("1970-01-01 00:00:01Z")), int) is True

    # date
    assert any2int(date(1, 1, 1)) == int_
    assert isinstance(any2int(date(1, 1, 1)), int) is True

    # timedelta
    dt = datetime(1970, 1, 1, 0, 0, 0)
    assert any2int(dt - datetime(1969, 12, 31, 23, 59, 59)) == int_
    assert any2int(dt - datetime(1969, 12, 31, 23, 59, 59, 1)) == int_
    assert any2int(dt - datetime(1969, 12, 31, 23, 59, 58, 999999)) == int_

    # boolean
    assert any2int(True) == 1
    assert any2int(False) == 0

    # other type
    with pytest.raises(ValueError) as excinfo:
        any2int("Hello".encode("utf-8"))


if __name__ == "__main__":
    import py
    py.test.cmdline.main("--tb=native -s")
