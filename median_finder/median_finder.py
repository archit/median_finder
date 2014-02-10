class Tree(object):
    """
    Represents a Binary tree
    """
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __getattr__(self, name):
        """ Delegate all other methods to the data payload """
        return getattr(self.data, name)

class Bucket(object):
    """
    Objects of this class simulate a memory limited list of numbers.
    It supports operations
    - insert_number
    - get_median
    - get_max
    - get_min
    - is_full

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

    def get_median(self, k=None):
        """ Get the k-th order statistic from the numbers in this bucket. Defaults to the median. """
        if k is None:
            k = len(self.numbers) // 2
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

    def __getattr__(self, name):
        """ Delegate all other methods to the conained list of numbers """
        return getattr(self.numbers, name)

class SophisticatedMedianFinder(object):
    """
    Represents a heap like tree structure, where each node is represented by
    `Bucket`, of a given batch_size
    """
    def __init__(self, batch_size):
        self.bucket_size = batch_size
        self.root_bucket = Tree(Bucket(self.bucket_size))
        self.total_numbers = 0

    def insert(self, a_number):
        """ Insert a number in the data structure. """
        self.total_numbers += 1
        self.insert_number(a_number, self.root_bucket)

    def insert_number(self, a_number, node):
        """ This is a tree sort insert algorithm. """
        if node.data.is_full():
            if self.node_contains(node, a_number):
                # Decide which `side` we're going to bump. Before inserting
                # the number in the bucket, we pick the side, and bump the
                # `last` number from that side of the bucket down the tree.
                # Defaults to the `left` side.
                if node.left:
                    orphaned_number = node.pop(0)
                    new_bucket = node.left
                elif node.right:
                    orphaned_number = node.pop()
                    new_bucket = node.right
                else:
                    orphaned_number = node.pop(0)
                    new_bucket = node.left = Tree(Bucket(self.bucket_size))

                node.insert_number(a_number)
                self.insert_number(orphaned_number, new_bucket)
            elif a_number < node.get_min():
                if node.left == None:
                    node.left = Tree(Bucket(self.bucket_size, [a_number]))
                else:
                    self.insert_number(a_number, node.left)
            elif node.get_max() < a_number:
                if node.right == None:
                    node.right = Tree(Bucket(self.bucket_size, [a_number]))
                else:
                    self.insert_number(a_number, node.right)
        else:
            node.insert_number(a_number)

    def node_contains(self, node, a_number):
        """ Predicate to check if `a_number` should belong to the `bucket` in `node` """
        return a_number >= node.get_min() and a_number <= node.get_max()

    def inorder_walk(self, start_node, visit):
        """ Perform an inorder traversal of the tree.
        Also supports aborting the walk, if the visit lambda returns False """
        iter_node = start_node
        next_node = []
        while next_node or iter_node:
            if iter_node:
                next_node.append(iter_node)
                iter_node = iter_node.left
            else:
                iter_node = next_node.pop()
                if visit(iter_node) == False:
                    break
                iter_node = iter_node.right


    def get_median(self):
        """ Do a tree sort search for bucket which will contain the median """
# Debug:
#        self.inorder_walk(self.root_bucket, lambda node: print("node={}".format(node.numbers)))

        i = 0
        target_node = None
        def find_median(node):
            i += len(node.numbers)
            if i > (self.total_numbers // 2):
                target_node = node
                return False
            else:
                return True
        self.inorder_walk(self.root_bucket, find_median)
        return target_node.get_median(i - (self.total_numbers // 2) - 1)

class NaiveMedianFinder(object):
    """
    A naive implementatin of finding the median of a list of numbers
    by using a simple array and in memory sort.
    """
    def __init__(self, batch_size):
        self.numbers = []

    def insert(self, a_number):
        self.numbers.append(a_number)

    def get_median(self):
        return sorted(self.numbers)[len(self.numbers) // 2]

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
