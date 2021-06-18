"""
Copy List with Random Pointer:

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
Return a deep copy of the list.
The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:
val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.
https://leetcode.com/problems/copy-list-with-random-pointer/
"""


# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next


class Solution:
    def copyRandomList(self, head):

        result = Node(-1)

        curr = result
        store = {}
        while head is not None:
            # create node
            if head not in store:
                new_node = Node(head.val)
                store[head] = new_node  # add node to store
            else:
                new_node = store[head]

            # create random
            if head.random is not None:
                if head.random not in store:
                    new_random = Node(head.random.val)
                    new_node.random = new_random
                    store[head.random] = new_random  # add node to store
                else:
                    new_node.random = store[head.random]

            # next
            curr.next = new_node
            curr = new_node

            head = head.next

        return result.next
