"""
Max Path Sum In Binary Tree:

Write a function that takes in a Binary Tree and returns its max path sum.
A path is a collection of connected nodes in a tree,
 where no node is connected to more than two other nodes;
 a path sum is the sum of the values of the nodes in a particular path.
Each BinaryTree node has an integer value, a left child node, and a right child node.
Children nodes can either be BinaryTree nodes themselves or None / null.

Sample Input
    tree = 1
        /     \
    2       3
    /   \   /   \
    4     5 6     7
Sample Output
    18 // 5 + 2 + 1 + 3 + 7
https://www.algoexpert.io/questions/Max%20Path%20Sum%20In%20Binary%20Tree
"""


class TreeInfo:

    def __init__(self, max_as_branch, max_as_branch_or_triangle):
        self.max_as_branch = max_as_branch
        # max continuous path as branch/tree
        self.max_as_branch_or_triangle = max_as_branch_or_triangle


# O(n) time
# O(log(n)) space - because it is a binary tree
def maxPathSum(tree):
    res = maxPathSumHelper(tree)
    return res.max_as_branch_or_triangle


def maxPathSumHelper(tree) -> TreeInfo:
    if not tree:
        # handle negatives with float('-inf')
        # return TreeInfo(float('-inf'), float('-inf')) # <- also works.
        return TreeInfo(0, float('-inf'))

    left = maxPathSumHelper(tree.left)
    right = maxPathSumHelper(tree.right)

    # longest continuous branch/straight line.
    curr_max_as_branch = max(
        tree.value,
        tree.value + left.max_as_branch,
        tree.value + right.max_as_branch
    )

    # longest tree/diameter/triangle/as a root node.
    curr_max_as_triangle = max(
        curr_max_as_branch,
        tree.value + left.max_as_branch + right.max_as_branch,

    )

    # longest branch/triangle we have seen so far.
    curr_max_as_branch_or_triangle = max(
        curr_max_as_triangle,
        left.max_as_branch_or_triangle,
        right.max_as_branch_or_triangle
    )

    return TreeInfo(curr_max_as_branch, curr_max_as_branch_or_triangle)
