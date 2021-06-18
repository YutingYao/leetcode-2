"""
Reverse Linked List
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# O(n) time | O(1) space
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        current = head
        prev = None

        while current is not None:
            # store next because we will loose track of it
            nxt = current.next

            # reverse pointer (point backwords)
            current.next = prev

            # # move on to next node
            # in the next iteration, the current current will be the prev
            prev = current
            # in the next iteration, the current current.next will be the current
            current = nxt

        return prev
