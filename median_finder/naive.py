import math

class NaiveMedianFinder(object):
    """
    A naive implementation of finding the median of a list of numbers
    by using a simple array and in memory sort.
    """
    def __init__(self, batch_size):
        self.numbers = []

    def insert(self, a_number):
        self.numbers.append(a_number)

    def get_median(self):
        if self.numbers:
            return sorted(self.numbers)[math.ceil(len(self.numbers) / 2) - 1]
        else:
            return None
