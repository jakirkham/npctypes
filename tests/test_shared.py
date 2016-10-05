#!/usr/bin/env python

__author__ = "John Kirkham <kirkhamj@janelia.hhmi.org>"
__date__ = "$Oct 05, 2016 9:46$"


import doctest
import sys
import unittest

from npctypes import shared


# Load doctests from `shared`.
def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(shared))
    return tests


if __name__ == '__main__':
    sys.exit(unittest.main())
