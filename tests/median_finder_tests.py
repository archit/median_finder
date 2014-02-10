from nose.tools import *
import os
import median_finder.median_finder

def test_input1():
    with open(os.path.abspath("tests/input1.txt")) as file:
        assert median_finder.find_median(file, 30) == median_finder.find_median(file, 30, median_finder.NaiveMedianFinder)

def test_input2():
    with open(os.path.abspath("tests/input2.txt")) as file:
        assert median_finder.find_median(file, 30) == median_finder.find_median(file, 30, median_finder.NaiveMedianFinder)
