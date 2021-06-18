"""
Linked List Cycle II

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Notice that you should not modify the linked list
https://leetcode.com/problems/linked-list-cycle-ii/
"""


class Solution:
    def detectCycle(self, head):
        if not head:
            return None

        fast = head
        slow = head

        # find cycle
        while True:
            if fast is None or fast.next is None:
                return None

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break

        one = head
        two = fast
        # find cycle start
        while one != two:
            one = one.next
            two = two.next
        return one


"""
Find Loop:
Write a function that takes in the head of a Singly Linked List that contains a loop 
(in other words, the list's tail node points to some node in the list instead of None / null). 
The function should return the node (the actual node--not just its value) from which the loop originates in constant space.
Each LinkedList node has an integer value as well as a next node pointing to the next node in the list.

Sample Input
    head = 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 // the head node with value 0
                            ^         v
                            9 <- 8 <- 7
Sample Output
    4 -> 5 -> 6 // the node with value 4
    ^         v
    9 <- 8 <- 7
https://www.algoexpert.io/questions/Find%20Loop
"""


# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def findLoop(head):
    # .next to allow the first loop to work
    p_one = head.next
    p_two = head.next.next

    # find meeting point
    while p_two != p_one:
        p_one = p_one.next
        p_two = p_two.next.next

    # find start of cycle
    p_one = head
    while p_two != p_one:
        p_one = p_one.next
        p_two = p_two.next

    return p_one
