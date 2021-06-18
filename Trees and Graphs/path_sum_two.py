"""
Leetcode 113: Path Sum II

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
Note: A leaf is a node with no children.
"""


# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# O(n) time | O(n) space
class Solution:
    def pathSum(self, root, sum):
        all_paths = []
        self._path_finder(root, sum, [], all_paths)
        return all_paths

    def _path_finder(self, curr, s, curr_path, allPaths):
        if curr is None:
            return

        # # gives us eror solvalble by backtracking
        # curr_path.append(curr.val)
        # curr_path  += [curr.val]
        curr_path = curr_path + [curr.val]
        s = s - curr.val

        # if the current node is a leaf and subrating it from s will give you 0, we have found a path, save the current path
        if s == 0 and not curr.left and not curr.right:
            # add's empy list ??? when I use curr_path.append(curr.val)
            allPaths.append(curr_path)
            # allPaths.append(list(curr_path)) # use this instead when using curr_path.append(curr.val)

        else:
            # traverse the left & right sub-tree
            self._path_finder(curr.left,
                              s, curr_path, allPaths)
            self._path_finder(curr.right,
                              s, curr_path, allPaths)

        # # incase we use curr_path.append(curr.val) instead of curr_path = curr_path + [curr.val] above, we will have to backtrack
        # remove the current node from the path to backtrack,
        # we need to remove the current node while we are going up the recursive call stack.
        # del curr_path[-1]


"""
Example:

Given the below binary tree and sum = 22,

        5
        / \
        4   8
    /   / \
    11  13  4
    /  \    / \
    7    2  5   1
Return:

    [
    [5,4,11,2],
    [5,8,4,5]
    ]
"""
