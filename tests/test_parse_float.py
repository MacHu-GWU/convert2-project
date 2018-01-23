#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from pytest import raises, approx
import numpy as np
import pandas as pd
from datetime import datetime, date
from convert2 import any2float


def test_parse_float():
    int_ = 1
    float_ = 1.0
    e = 0.00000001

    # None
    assert any2float(None) is None
    assert any2float(np.nan) is None

    # int, long, np.int, np.int8, np.int16, np.int32, np.int64
    assert abs(any2float(int_) - float_) <= e
    assert abs(any2float(np.int(int_)) - float_) <= e
    assert abs(any2float(np.int8(int_)) - float_) <= e
    assert abs(any2float(np.int16(int_)) - float_) <= e
    assert abs(any2float(np.int32(int_)) - float_) <= e
    assert abs(any2float(np.int64(int_)) - float_) <= e
    assert abs(any2float(int_) - float_) <= e
    assert abs(any2float(-int_) - (-float_)) <= e
    assert abs(any2float(np.int64(int_)) - float_) <= e
    assert abs(any2float(np.int64(-int_)) - (-float_)) <= e

    # float, np.float, np.float16, np.float32, np.float64
    assert abs(any2float(float_) - float_) <= e
    assert abs(any2float(np.float(float_)) - float_) <= e
    assert abs(any2float(np.float16(float_)) - float_) <= e
    assert abs(any2float(np.float32(float_)) - float_) <= e
    assert abs(any2float(np.float64(float_)) - float_) <= e

    # str, unicode, np.str
    assert abs(any2float("1") - float_) <= e
    assert abs(any2float("1.0") - float_) <= e
    assert abs(any2float("a1b") - float_) <= e
    assert abs(any2float("a 1.0 b") - float_) <= e

    with raises(ValueError) as excinfo:
        any2float("a1b2c")

    with raises(ValueError) as excinfo:
        any2float("a1.1b2.2c")

    assert any2float(u"1") == approx(float_)
    assert any2float(u"1.0") == approx(float_)
    assert any2float(u"a1b") == approx(float_)
    assert any2float(u"a 1.0 b") == approx(float_)

    assert any2float(np.str("1")) == approx(float_)
    assert any2float(np.str("1.0")) == approx(float_)
    assert any2float(np.str("a1b")) == approx(float_)
    assert any2float(np.str("a 1.0 b")) == approx(float_)

    any2float.EXTRACT_NUMBER_FROM_TEXT = False
    with pytest.raises(ValueError) as excinfo:
        any2float("a1b")
    any2float.EXTRACT_NUMBER_FROM_TEXT = True

    # datetime, np.datetime64, pd.tslib.Timestamp
    assert any2float(datetime(1970, 1, 1, 0, 0, 1)) == approx(float_)
    assert any2float(np.datetime64("1970-01-01 00:00:01Z")) == approx(float_)
    assert any2float(pd.Timestamp("1970-01-01 00:00:01Z")) == approx(float_)

    assert isinstance(any2float(datetime(1970, 1, 1, 0, 0, 1)), float) is True
    assert isinstance(
        any2float(np.datetime64("1970-01-01 00:00:01Z")), float) is True
    assert isinstance(
        any2float(pd.Timestamp("1970-01-01 00:00:01Z")), float) is True

    # date
    assert any2float(date(1, 1, 1)) == approx(float_)
    assert isinstance(any2float(date(1, 1, 1)), float) is True

    # timedelta
    dt = datetime(1970, 1, 1, 0, 0, 0)
    assert any2float(dt - datetime(1969, 12, 31, 23, 59, 59))  == approx(float_)

    # boolean
    assert any2float(True) == approx(1.)
    assert any2float(False) == approx(0.)

    # other type
    with pytest.raises(ValueError) as excinfo:
        any2float("Hello".encode("utf-8"))


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
