#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Test isinstance(obj, type) behavior in between python naive, numpy type,
pandas type.
"""

import pytest
from datetime import datetime
import numpy as np
import pandas as pd
from convert2.pkg.six import PY3, PY2


def test_is_int():
    # is int
    assert isinstance(1, int) is True
    assert isinstance(np.int(1), int) is True
    assert isinstance(np.int8(1), int) is False
    assert isinstance(np.int16(1), int) is False

    if PY3:
        assert isinstance(np.int32(1), int) is False
    elif PY2:
        assert isinstance(np.int32(1), int) is True

    assert isinstance(np.int64(1), int) is False

    # is np.int
    assert isinstance(np.int(1), np.int) is True
    assert isinstance(np.int8(1), np.int) is False
    assert isinstance(np.int16(1), np.int) is False

    if PY3:
        assert isinstance(np.int32(1), np.int) is False
    elif PY2:
        assert isinstance(np.int32(1), np.int) is True

    assert isinstance(np.int64(1), np.int) is False


def test_is_float():
    # is float
    assert isinstance(1.0, float) is True
    assert isinstance(np.float(1.0), float) is True
    assert isinstance(np.float16(1.0), float) is False
    assert isinstance(np.float32(1.0), float) is False
    assert isinstance(np.float64(1.0), float) is True

    # is np.float
    assert isinstance(1.0, np.float) is True
    assert isinstance(np.float(1.0), np.float) is True
    assert isinstance(np.float16(1.0), np.float) is False
    assert isinstance(np.float32(1.0), np.float) is False
    assert isinstance(np.float64(1.0), np.float) is True


def test_is_str():
    assert isinstance("Hello", str) is True
    assert isinstance("Hello", np.str) is True


def test_is_datetime():
    assert isinstance(datetime.now(), datetime) is True
    assert isinstance(np.datetime64("1970-01-01 00:00:00Z"), datetime) is False
    assert isinstance(
        pd.tslib.Timestamp("1970-01-01 00:00:00Z"), datetime) is True


def test_is_None():
    assert None is None
    assert np.nan is np.nan


def test_data_read_from_pandas():
    df = pd.read_csv("data.txt")
    record = df.loc[0, :]
    assert isinstance(record._int, np.int64) is True
    assert isinstance(record._float, float) is True
    assert isinstance(record._str, str) is True
    assert isinstance(record._datetime, str) is True
    assert isinstance(record._date, str) is True
    assert record._none, None


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
