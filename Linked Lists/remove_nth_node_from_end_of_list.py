"""
Remove Nth Node From End of List:

Given the head of a linked list, remove the nth node from the end of the list and return its head.
Follow up: Could you do this in one pass?
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int):

        # keep distance
        left = head
        right = head.next
        count = 1
        while count != n:
            count += 1
            right = right.next

        # find end
        prev_left = None
        while right is not None:
            prev_left = left
            left = left.next
            right = right.next

        # remove
        if count == 1 and prev_left is None and right is None:  # list has single element
            return None
        elif prev_left is None:  # remove head
            return head.next

        prev_left.next = left.next
        return head
