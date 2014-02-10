class Bucket(object):
    """
    Objects of this class simulate a memory limited list of numbers.

    It also proxies any other methods straight to the list implementation
    contained within.
    """
    def __init__(self, size, seed_numbers=None):
        self.size = size
        if seed_numbers is None:
            seed_numbers = []
        self.numbers = seed_numbers

    def insert_number(self, a_number):
        """ Insert a number in this bucket using the insertion-sort strategy """
        # Due dilligence check.
        if self.is_full():
            raise "Bucket is full!"

        i = 0
        for number in self.numbers:
            if number > a_number:
                break
            else:
                i += 1
        self.numbers.insert(i, a_number)

    def get_statistic(self, k=None):
        """ Get the k-th order statistic from the numbers in this bucket. Defaults to the median. """
        if k is None:
            k = math.ceil(len(self.numbers) / 2) - 1
        return self.numbers[k]

    def get_max(self):
        """ Get the maximum of the numbers in this bucket """
        return self.numbers[len(self.numbers) - 1]

    def get_min(self):
        """ Get the minimum of the numbers in this bucket """
        return self.numbers[0]

    def is_full(self):
        """ Returns if the bucket is at capacity """
        return len(self.numbers) >= self.size

    def in_range(self, a_number):
        """ Predicate to check if `a_number` should belong to the `bucket` in `node` """
        return a_number >= self.get_min() and a_number <= self.get_max()

    def __getattr__(self, name):
        """ Delegate all other methods to the conained list of numbers """
        return getattr(self.numbers, name)
