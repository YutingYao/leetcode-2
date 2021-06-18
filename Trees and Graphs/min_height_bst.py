"""
Min Height BST:
Write a function that takes in a non-empty sorted array of distinct integers, constructs a BST from the integers, and returns the root of the BST.
The function should minimize the height of the BST.
You've been provided with a BST class that you'll have to use to construct the BST.
Each BST node has an integer value, a left child node, and a right child node. 
A node is said to be a valid BST node if and only if it satisfies the BST property:
 its value is strictly greater than the values of every node to its left; its value is less than or equal to the values of every node to its right;
  and its children nodes are either valid BST nodes themselves or None / null.
A BST is valid if and only if all of its nodes are valid BST nodes.
Note that the BST class already has an insert method which you can use if you want.

Sample Input
array = [1, 2, 5, 7, 10, 13, 14, 15, 22]
Sample Output
         10
       /     \
      2      14
    /   \   /   \
   1     5 13   15
          \       \
           7      22
// This is one example of a BST with min height
// that you could create from the input array.
// You could create other BSTs with min height
// from the same array; for example:
         10
       /     \
      5      15
    /   \   /   \
   2     7 13   22
 /           \
1            14
https://www.algoexpert.io/questions/Min%20Height%20BST
"""


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)


def minHeightBst1(array):
    # find the BST's most appropriate head
    first_middle = (len(array) // 2)
    head = BST(array[first_middle])

    def minBstHelper(left, right):
        length = (right - left) + 1
        if length == 0 or right < left:
            return
        elif length == 1:
            head.insert(array[left])
            return

        middle = (length // 2)
        head.insert(array[left+middle])

        # deal with the rest of the array (ignoring the middle element as we have already inserted it)
        minBstHelper(0, middle-1)  # left half
        minBstHelper(middle+1, len(array)-1)  # right half

    # deal with the array in halves
    minBstHelper(0, first_middle-1)
    minBstHelper(first_middle+1, len(array))

    return head


def minHeightBstHelper(array, bst, start_idx, end_idx):
    if start_idx > end_idx:
        return

    mid_idx = (start_idx + end_idx) // 2
    new_node = BST(array[mid_idx])

    if bst is None:
        bst = new_node
    else:
        if array[mid_idx] < bst.value:
            bst.left = new_node
            bst = bst.left
        else:
            bst.right = new_node
            bst = bst.right

    minHeightBstHelper(array, bst, start_idx, mid_idx-1)
    minHeightBstHelper(array, bst, mid_idx+1, end_idx)
    return bst


def minHeightBst(array):
    return minHeightBstHelper(array, None, 0, len(array)-1)


def minHeightBst10(array):
    return minHeightBstHelper10(array, 0, len(array)-1)


def minHeightBstHelper10(array, left, right):
    if right-left < 0:
        return None

    mid = (right+left) // 2
    node = BST(array[mid])

    node.left = minHeightBstHelper10(array, left, mid-1)
    node.right = minHeightBstHelper10(array, mid+1, right)

    return node
