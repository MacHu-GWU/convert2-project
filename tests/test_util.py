#!/usr/bin/env python
# -*- coding: utf-8 -*-

from convert2.util import extract_number_from_string


def test_extract_number_from_string():
    assert extract_number_from_string("1") == ["1"]
    assert extract_number_from_string("1.001") == ["1.001"]
    assert extract_number_from_string("0.999") == ["0.999"]

    assert extract_number_from_string("a 1 b . c") == ["1"]
    assert extract_number_from_string("a 1.001 b . c") == ["1.001"]
    assert extract_number_from_string("a 0.999 b . c") == ["0.999"]

    assert extract_number_from_string(".") == []
    assert extract_number_from_string("a1b2c") == ["1", "2"]


if __name__ == "__main__":
    import py
    py.test.cmdline.main("--tb=native -s")
