"""
Reverse Linked List II: Leetcode 92

Reverse a linked list from position m to n. Do it in one-pass.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        pos = 1

        curr = head
        prev: ListNode = None

        #  # iterate till the position where we find the section to be reversed
        while pos < m:
            # move to next node
            prev = curr
            curr = curr.next

            pos += 1

        # store the last non reversed(not to be reversed) node
        last_none_reversed_node = prev
        # will be the tail of the last reversed list
        reversed_list_tail = curr

        #  # revese a section of the list
        while pos <= n:
            nxt = curr.next

            # reverse pointer
            curr.next = prev

            # move on to next node
            prev = curr
            curr = nxt

            pos += 1

        # # fix the reversed list position in the larger list
        if last_none_reversed_node is not None:
            # last_none_reversed_node.next = last revered node
            last_none_reversed_node.next = prev
        # handle situation where we reversed from 1
        else:
            # if we started reversing from 1, then the last item reversed will be put at 1 (head)
            head = prev

        # connect the reversed list's tail to the the (n+1) node
        reversed_list_tail.next = curr

        return head


"""
Input:
    [1,2,3,4,5,6,7,8,9,10,11,12,13]
    3
    8
    [5]
    1
    1
    [3,5]
    1
    1
    [3,5]
    1
    2
Output:
    [1,2,8,7,6,5,4,3,9,10,11,12,13]
    [5]
    [3,5]
    [5,3]
"""
