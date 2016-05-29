#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import numpy as np, pandas as pd
import unittest

def isnull(value):
    """There is no universal function can exam is ``None`` type or ``np.nan``.
    
    This one is the best approach so far. 
    """
    if value is None or value is np.nan:
        return True
    else:
        return False
    
class HandleNA(unittest.TestCase):
    """Test :func:`isnull` function
    """
    def test_all(self):
        self.assertTrue(isnull(None))
        self.assertTrue(isnull(np.nan))
        self.assertFalse(isnull(True))
        self.assertFalse(isnull(False))
        self.assertFalse(isnull(""))
        
if __name__ == "__main__":
    import py
    py.test.cmdline.main("--tb=native -s")