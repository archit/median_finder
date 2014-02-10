import os
from nose.tools import *
from median_finder.median_finder import *

# Courtesy http://stackoverflow.com/questions/845058/how-to-get-line-count-cheaply-in-python
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

# Test working with files
def test_files():
    for filename in ["input1", "input2"]:
        filename_with_path = os.path.abspath("tests/{}.txt".format(filename))
        for bucket_size in range(1, file_len(filename_with_path)):
            with open(filename_with_path) as file:
                actual   = find_median(file, bucket_size)
            with open(filename_with_path) as file:
                expected = find_median(file, bucket_size, NaiveMedianFinder)
            eq_(expected, actual, "{} != {} (bucket_size={})".format(expected, actual, bucket_size))

def test_empty_stream():
    eq_(find_median([], 3), None)
