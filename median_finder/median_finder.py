import math
from median_finder.sophisticated import *

def find_median(number_stream, batch_size=50, find_strategy=SophisticatedMedianFinder):
    """
    The main interface for the median finder.

    number_stream - An iterable stream of numbers
    batch_size    - Maximum number of numbers one bucket/machine
                      can hold at a itme. Defaults to 50.
    find_strategy - Which median finding strategy to use. Options are
                      NaiveMedianFinder
                      SophisticatedMedianFinder
    """
    median_finder = find_strategy(batch_size)
    for line in number_stream:
        median_finder.insert(int(line))
    return median_finder.get_median()
