import math
from median_finder.tree import *
from median_finder.bucket import *

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
            if node.in_range(a_number):
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

    def get_median(self):
        """ Do a tree sort search for bucket which will contain the median """
        if len(self.root_bucket.numbers) == 0:
            return None

        i = 0
        median_location = math.ceil(self.total_numbers / 2)
        for node in self.root_bucket.inorder_walker():
            i += len(node.numbers)
            if i >= median_location:
                target_node = node
                break

        return target_node.get_statistic(len(target_node.numbers) - (i - median_location) - 1)

    def __str__(self):
        ret = ""
        for node in self.root_bucket.inorder_walker():
            ret += "{}".format(node.numbers)
        return ret
