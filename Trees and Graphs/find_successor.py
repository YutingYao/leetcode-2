"""
Find Successor:

Write a function that takes in a Binary Tree (where nodes have an additional pointer to their parent node)
 as well as a node contained in that tree and returns the given node's successor.
A node's successor is the next node to be visited (immediately after the given node) 
 when traversing its tree using the in-order tree-traversal technique.
A node has no successor if it's the last node to be visited in the in-order traversal.
If a node has no successor, your function should return None / null.
Each BinaryTree node has an integer value, a parent node, a left child node, and a right child node.
Children nodes can either be BinaryTree nodes themselves or None / null.

https://www.algoexpert.io/questions/Find%20Successor
"""


# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


# find successor
def findSucc(tree):
    # check if we have a right subtree and find successor through it
    if tree.right is not None:
        # find leftmost child of right subtree
        curr = tree.right
        while curr.left is not None:
            curr = curr.left
        return curr

    # find successor through parent
    else:
        curr = tree
        while curr is not None:

            if curr.parent is None:  # no successor
                return None

            # if curr is the parent's left child then the parent is the successor
            elif curr.parent.left == curr:
                return curr.parent

            else:  # curr.parent.right == curr
                curr = curr.parent


def traverse(tree, node):
    if tree is None:
        return None

    left_subtree = traverse(tree.left, node)

    if tree.value == node.value:  # check for node
        return findSucc(tree)  # found node, so find successor

    right_subtree = traverse(tree.right, node)

    return left_subtree or right_subtree


# lnr
def findSuccessor1(tree_node, node):
    return traverse(tree_node, node)


# O(h) time
def findSuccessor(tree, node):
    return findSucc(node)


# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor10(tree, node):

    if tree == node:
        res = getSuccessor(tree)
        return res

    l = r = None
    if tree.left:
        l = findSuccessor10(tree.left, node)
    if tree.right:
        r = findSuccessor10(tree.right, node)
    return l or r


def getSuccessor(tree):

    # if has a right child
    # will be left most node of right child
    if tree.right is not None:
        curr = tree.right
        while curr.left is not None:
            # print(curr.left.value)
            curr = curr.left
        return curr

    # no right child -> successor is ancestor:
    # find ancestor where child is left child
    else:
        curr = tree
        while curr.parent is not None and curr != curr.parent.left:
            curr = curr.parent

        return curr.parent
