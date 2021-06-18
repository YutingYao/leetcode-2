"""
Construct Binary Tree from Preorder and Inorder Traversal:

Given preorder and inorder traversal of a tree, construct the binary tree.
Note:
You may assume that duplicates do not exist in the tree.
"""


from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]):
        preorder_pos = 0
        inorder_idxs = {val: idx for idx, val in enumerate(inorder)}

        def helper(preorder: List[int], inorder: List[int], inorder_left, inorder_right):
            nonlocal preorder_pos

            if inorder_right - inorder_left < 0 or preorder_pos >= len(preorder):
                return None

            val = preorder[preorder_pos]
            node = TreeNode(val)
            ino_idx = inorder_idxs[val]

            # next
            preorder_pos += 1

            node.left = helper(
                preorder, inorder, inorder_left, ino_idx - 1)
            node.right = helper(
                preorder, inorder, ino_idx+1, inorder_right)

            return node

        return helper(preorder, inorder, 0, len(inorder)-1)


class Solution0:
    def buildTree(self, preorder: List[int], inorder: List[int]):

        if len(inorder) == 0:
            return None

        if len(preorder) == 1:
            return TreeNode(preorder[0])

        ino_index = inorder.index(preorder.pop(0))
        node = TreeNode(inorder[ino_index])

        node.left = self.buildTree(preorder, inorder[:ino_index])
        node.right = self.buildTree(preorder, inorder[ino_index+1:])

        return node


class Solution01:
    def buildTree(self, preorder: List[int], inorder: List[int], preorder_pos):

        if len(inorder) == 0:
            return None

        if preorder_pos >= len(preorder):
            return None
        ino_index = inorder.index(preorder[preorder_pos])
        node = TreeNode(inorder[ino_index])

        preorder_pos += 1

        node.left = self.buildTree(
            preorder, inorder[:ino_index], preorder_pos)
        node.right = self.buildTree(
            preorder, inorder[ino_index+1:], preorder_pos)

        return node


class Solution1(object):
    preorder = []
    inorder = []

    def buildTree(self, preorder, inorder):
        self.preorder = preorder
        self.inorder = inorder
        return self.dfs(0, len(self.preorder), 0, len(self.inorder))

    def dfs(self, pre_start, pre_end, in_start, in_end):  # [start, end)
        if pre_end - pre_start <= 0:
            return None
        root = TreeNode(self.preorder[pre_start])
        offset = self.inorder[in_start: in_end +
                              1].index(self.preorder[pre_start])

        root.left = self.dfs(pre_start+1, pre_start+1 +
                             offset, in_start, in_start+offset)
        root.right = self.dfs(pre_start+1+offset, pre_end,
                              in_start+1+offset, in_end)
        return root


class Solution2(object):
    def buildTree(self, preorder, inorder):
        return self.dfs(preorder, inorder)

    def dfs(self, preorder, inorder):
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        root_idx = inorder.index(preorder[0])
        root.left = self.dfs(preorder[1: root_idx+1], inorder[: root_idx])
        root.right = self.dfs(preorder[root_idx+1:], inorder[root_idx+1:])
        return root
