class Tree(object):
    """
    Represents a Binary tree
    """
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def inorder_walker(self):
        """ Perform an inorder traversal of the tree using generators. """
        iter_node = self
        next_node = []
        while next_node or iter_node:
            if iter_node:
                next_node.append(iter_node)
                iter_node = iter_node.left
            else:
                iter_node = next_node.pop()
                yield iter_node
                iter_node = iter_node.right

    def __getattr__(self, name):
        """ Delegate all other methods to the data payload """
        return getattr(self.data, name)
