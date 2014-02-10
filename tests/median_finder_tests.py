from nose.tools import *
import os
from median_finder.median_finder import *

def test_all():
    BUCKET_SIZE = 5
    for filename in ["input1", "input2"]:
        with open(os.path.abspath("tests/{}.txt".format(filename))) as file:
            actual   = find_median(file, BUCKET_SIZE)
        with open(os.path.abspath("tests/{}.txt".format(filename))) as file:
            expected = find_median(file, BUCKET_SIZE, NaiveMedianFinder)
        print("Using size={}, expected={}, actual={}", BUCKET_SIZE, expected, actual)
        assert expected == actual
