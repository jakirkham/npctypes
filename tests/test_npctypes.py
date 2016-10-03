#!/usr/bin/env python

__author__ = "John Kirkham <kirkhamj@janelia.hhmi.org>"
__date__ = "$Oct 03, 2016 14:19$"


import doctest
import sys
import unittest

from npctypes import npctypes


# Load doctests from `npctypes`.
def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(npctypes))
    return tests


if __name__ == '__main__':
    sys.exit(unittest.main())
