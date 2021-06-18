"""
Binary Tree Inorder Traversal:

Given the root of a binary tree, return the inorder traversal of its nodes' values.
https://leetcode.com/problems/binary-tree-inorder-traversal/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def inorderTraversal(self, root):
        output = []
        self.inorderTraversalHelper(root, output)
        return output

    def inorderTraversalHelper(self, root, output):
        if not root:
            return

        self.inorderTraversalHelper(root.left, output)
        output.append(root.val)
        self.inorderTraversalHelper(root.right, output)


class Solution:
    def inorderTraversal(self, root: TreeNode):
        output = []

        stack = []
        curr = root
        while curr is not None or len(stack) > 0:

            # add all left
            while curr is not None:
                stack.append(curr)
                curr = curr.left

            # visit node
            temp = stack.pop()
            output.append(temp.val)

            curr = temp.right

        return output
