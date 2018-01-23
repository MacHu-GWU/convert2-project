#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import pytest
import numpy as np
import pandas as pd
from datetime import datetime, date
from convert2 import any2str
from convert2.pkg.rolex import utc


def test_parse_str():
    """Test parse to str.
    """
    # None
    assert any2str(None) is None
    assert any2str(np.nan) is None

    # int, long, np.int, np.int8, np.int16, np.int32, np.int64
    assert any2str(1) == "1"
    assert any2str(np.int(1)) == "1"
    assert any2str(np.int8(1)) == "1"
    assert any2str(np.int16(1)) == "1"
    assert any2str(np.int32(1)) == "1"
    assert any2str(np.int64(1)) == "1"

    # float, np.float, np.float16, np.float32, np.float64
    assert any2str(3.14) == "3.14"
    assert any2str(np.float(3.14)) == "3.14"
    assert any2str(np.float32(3.14)) == "3.14"
    assert any2str(np.float64(3.14)) == "3.14"

    # str
    assert any2str("hello") == "hello"

    # datetime, np.datetime64, pd.tslib.Timestamp
    assert any2str(
        datetime(1970, 1, 1, 0, 0, 0, tzinfo=utc)) == "1970-01-01 00:00:00+00:00"
    assert any2str(
        pd.Timestamp("1970-01-01 00:00:01Z")) == "1970-01-01 00:00:01+00:00"

    # date
    assert any2str(date(1970, 1, 1)) == "1970-01-01"

    # bytes
    assert any2str("hello".encode("ascii")) == "hello"
    assert any2str("hello".encode("Windows-1252")) == "hello"
    assert any2str("hello".encode("ISO-8859-1")) == "hello"
    assert any2str("hello".encode("utf8")) == "hello"


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
