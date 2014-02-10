#!/usr/bin/env python3

import sys
from median_finder.median_finder import find_median

if len(sys.argv) < 3:
    print("Usage: python3 -m median_finder [bucket_size] [input_file]")
else:
    with open(sys.argv[2]) as file:
        print(find_median(file, int(sys.argv[1])))
