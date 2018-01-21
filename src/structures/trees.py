"""
Trees and Heap

Trees are data structures linking nodes in a tree-like structure: a unique
node constitutes the 'root' of the tree from which sprout 'branches' leading to
other nodes called 'children'.

Trees can be either represented by nested lists or by a Tree object. In this
module we show the object represnetation for a binary tree.

There exist three types of ways to traverse trees (ie visit all their nodes):
preorder, inorder and postorder. These methods are given below.
(TO BE IMPLEMENTED SOON)
"""


class Node:
    """
    Nodes contain a key and may carry some extra data called payload
    """
    def __init__(self, key, payload=None):
        self.key = key
        self.payload = payload


class BinaryTree:
    """
    A binary Tree is a common subtype of trees where each parent only accept a
    maximum of two children.

    The particularity of trees is that each node can be considered the root of
    a subtree. This leads to interesting recursive properties to walk the tree.
    """
    def __init__(self, root_node):
        self.node = root_node
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        """
        Insert a new node as the left child of the tree. If there is no left
        child already, the left child is directly added as the root of a new
        sub tree. Otherwise the current left_child is added as the left child
        of the new subtree which is itself inserted as left child of the
        current node.
        """
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        else:
            subtree = BinaryTree(new_node)
            subtree.left_child = self.left_child
            self.left_child = subtree

    def insert_right(self, new_node):
        """ same as above but with the right child """
        if self.right_child is None:
            self.right_child = BinaryTree(new_node)
        else:
            subtree = BinaryTree(new_node)
            subtree.right_child = self.right_child
            self.right_child = subtree

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.leftChild

    def set_root_value(self, obj):
        self.key = obj

    def get_root_value(self):
        return self.key
