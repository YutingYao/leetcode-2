"""
Implement Queue using Stacks:

Implement a first in first out (FIFO) queue using only two stacks.
The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).
Implement the MyQueue class:
    void push(int x) Pushes element x to the back of the queue.
    int pop() Removes the element from the front of the queue and returns it.
    int peek() Returns the element at the front of the queue.
    boolean empty() Returns true if the queue is empty, false otherwise.
Notes:
You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively. 
You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
Follow-up: 
Can you implement the queue such that each operation is amortized O(1) time complexity? 
In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.
https://leetcode.com/problems/implement-queue-using-stacks/
"""


class MyStack:

    def __init__(self):
        self.items = []

    def push(self, x: int):
        self.items.append(x)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def empty(self):
        return len(self.items) == 0


class MyQueue:

    def __init__(self):
        self.stack_one = MyStack()
        self.stack_two = MyStack()

    def push(self, x: int):
        # Push element x to the back of queue.
        self.stack_one.push(x)

    def pop(self):
        # Removes the element from in front of queue and returns that element.
        if self.stack_two.empty():
            self._moveStackOneItemsToStackTwo()

        return self.stack_two.pop()

    def peek(self):
        # Get the front element.
        if self.stack_two.empty():
            self._moveStackOneItemsToStackTwo()

        return self.stack_two.peek()

    def empty(self):
        # Returns whether the queue is empty.
        return self.stack_one.empty() and self.stack_two.empty()

    def _moveStackOneItemsToStackTwo(self):
        # reverse stack one
        while not self.stack_one.empty():
            self.stack_two.push(self.stack_one.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
