"""
Binary Tree Diameter:

Write a function that takes in a Binary Tree and returns its diameter. 
The diameter of a binary tree is defined as the length of its longest path, even if that path doesn't pass through the root of the tree.
A path is a collection of connected nodes in a tree, where no node is connected to more than two other nodes. 
The length of a path is the number of edges between the path's first node and its last node.
Each BinaryTree node has an integer value, a left child node, and a right child node. Children nodes can either be BinaryTree nodes themselves or None / null.
https://www.algoexpert.io/questions/Binary%20Tree%20Diameter
https://leetcode.com/problems/diameter-of-binary-tree/
"""


# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, diameter, height):
        self.diameter = diameter
        self.height = height


def binaryTreeDiameterHelper1(node):
    if node is None:
        return TreeInfo(0, 0)

    left_vals = binaryTreeDiameterHelper(node.left)
    right_vals = binaryTreeDiameterHelper(node.right)

    max_diameter_so_far = max(left_vals.diameter, right_vals.diameter)
    longest_path_through_node = left_vals.height + right_vals.height
    curr_height = 1 + max(left_vals.height, right_vals.height)

    # curr_max_diameter = max(max_diameter_so_far, curr_height-1) # not include current node in path/diameter
    curr_max_diameter = max(max_diameter_so_far, longest_path_through_node)

    return TreeInfo(curr_max_diameter, curr_height)


def binaryTreeDiameter1(tree):
    return binaryTreeDiameterHelper1(tree).diameter


def binaryTreeDiameterHelper(node):
    if node is None:
        # [diameter, height]
        return [0, 0]

    left_vals = binaryTreeDiameterHelper(node.left)
    right_vals = binaryTreeDiameterHelper(node.right)

    prev_max_diameter = max(left_vals[0], right_vals[0])

    curr_path = left_vals[1] + right_vals[1]
    curr_height = 1 + max(left_vals[1], right_vals[1])

    max_diameter = max(prev_max_diameter, curr_path)

    return [max_diameter, curr_height]


def binaryTreeDiameter(tree):
    return binaryTreeDiameterHelper(tree)[0]


def binaryTreeDiameter3(tree):
    max_diameter = [-1]
    depths(tree, max_diameter)
    return max_diameter[0]


def depths(node, max_diameter):
    if node is None:
        return 0

    # calculate diameter
    left = depths(node.left, max_diameter)
    right = depths(node.right, max_diameter)
    max_diameter[0] = max(max_diameter[0], left+right)

    return max(left, right) + 1  # add node to depth
