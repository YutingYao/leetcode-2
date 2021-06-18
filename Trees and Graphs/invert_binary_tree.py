"""
Invert Binary Tree:

Write a function that takes in a Binary Tree and inverts it. 
In other words, the function should swap every left node in the tree for its corresponding right node.
Each BinaryTree node has an integer value, a left child node, and a right child node. 
Children nodes can either be BinaryTree nodes themselves or None / null.
https://www.algoexpert.io/questions/Invert%20Binary%20Tree
"""
# This is the class of the input binary tree.


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def invertBinaryTreeHelper(node):
    if node is None:
        return

    prev_left = node.left
    node.left = node.right
    node.right = prev_left

    invertBinaryTreeHelper(node.left)
    invertBinaryTreeHelper(node.right)


def invertBinaryTree(tree):
    invertBinaryTreeHelper(tree)
    return tree
