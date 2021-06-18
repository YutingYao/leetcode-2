"""
Lowest Common Ancestor of a Binary Search Tree:

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
According to the definition of LCA on Wikipedia: 
“The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants
 (where we allow a node to be a descendant of itself).”
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        lowest = root

        while True:
            if lowest.val < p.val and lowest.val < q.val:
                lowest = lowest.right
            elif lowest.val > p.val and lowest.val > q.val:
                lowest = lowest.left
            else:
                break

        return lowest


"""
FIrst Approach:
- take advantage of BST's properties
"""
