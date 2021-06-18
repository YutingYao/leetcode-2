"""
Remove Kth Node From End:

Write a function that takes in the head of a Singly Linked List and an integer k and removes the kth node from the end of the list.
The removal should be done in place, meaning that the original data structure should be mutated (no new structure should be created).
Furthermore, the input head of the linked list should remain the head of the linked list after the removal is done,
 even if the head is the node that's supposed to be removed.
In other words, if the head is the node that's supposed to be removed, your function should simply mutate its value and next pointer.
Note that your function doesn't need to return anything.
You can assume that the input Linked List will always have at least two nodes and, more specifically, at least k nodes.
Each LinkedList node has an integer value as well as a next node pointing to the next node in the list or to None / null if it's the tail of the list.
https://www.algoexpert.io/questions/Remove%20Kth%20Node%20From%20End
"""


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) time | O(n) space
def removeKthNodeFromEnd(head, k):

    # find node positions
    positions = {}
    curr = head
    count = 1
    while curr is not None:
        positions[count] = curr
        curr = curr.next
        count += 1

    if k == 1:  # if node is the tail:
        before_to_delete = positions[(count-(k))-1]
        before_to_delete.next = None
    else:
        after_to_delete = positions[(count-(k))+1]
        to_delete = positions[count-(k)]
        to_delete.value = after_to_delete.value
        to_delete.next = after_to_delete.next

    return head


# O(n) time | O(1) space
def removeKthNodeFromEnd1(head, k):

    right = head
    left = head
    prev_left = None

    counter = 1
    # create length k space between right and left
    while counter <= k:
        right = right.next
        counter += 1

    # find end (move right past end)
    while right is not None:
        prev_left = left
        left = left.next
        right = right.next

    # delete
    if left.next is None:  # tail
        prev_left.next = None
    else:
        nxt = left.next
        left.value = nxt.value
        left.next = nxt.next

    return head


def removeKthNodeFromEnd4(head, k):
    left = right = head
    before_left = None

    counter = 1
    while counter <= k:
        right = right.next
        counter += 1

    while right is not None:
        right = right.next
        before_left = left
        left = left.next

    if before_left is None:  # remove head
        left.value = left.next.value
        left.next = left.next.next
    else:
        before_left.next = before_left.next.next
