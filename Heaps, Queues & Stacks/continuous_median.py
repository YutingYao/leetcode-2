"""
Continuous Median:
Write a ContinuousMedianHandler class that supports:
The continuous insertion of numbers with the insert method.
The instant (O(1) time) retrieval of the median of the numbers that have been inserted thus far with the getMedian method.
The getMedian method has already been written for you. You simply have to write the insert method.
The median of a set of numbers is the "middle" number when the numbers are ordered from smallest to greatest. 
If there's an odd number of numbers in the set, as in {1, 3, 7}, the median is the number in the middle (3 in this case);
 if there's an even number of numbers in the set, as in {1, 3, 7, 8}, the median is the average of the two middle numbers ((3 + 7) / 2 == 5 in this case).

Sample Usage
// All operations below are performed sequentially.
ContinuousMedianHandler(): - // instantiate a ContinuousMedianHandler
    insert(5): -
    insert(10): -
    getMedian(): 7.5
    insert(100): -
    getMedian(): 10
https://www.algoexpert.io/questions/Continuous%20Median
"""

import heapq


class ContinuousMedianHandlerBF:
    def __init__(self):
        # Write your code here.
        self.median = None
        self.small_nums = []
        self.big_nums = []

    def insert(self, number):
        if len(self.small_nums) > 0 and -self.small_nums[0] > number:
            heapq.heappush(self.small_nums, -number)
        else:
            heapq.heappush(self.big_nums, number)
        self.balance_heaps()
        self.update_median()
        # self.print_heaps()

    def getMedian(self):
        return self.median

    def balance_heaps(self):

        while len(self.big_nums) - len(self.small_nums) >= 2:
            heapq.heappush(self.small_nums, -
                           heapq.heappop(self.big_nums))

        while len(self.small_nums) - len(self.big_nums) >= 1:
            heapq.heappush(self.big_nums, -
                           heapq.heappop(self.small_nums))

    def update_median(self):
        is_even = (len(self.big_nums) + len(self.small_nums)) % 2 == 0
        if is_even:
            self.median = (self.big_nums[0] + (-self.small_nums[0])) / 2
        else:
            self.median = self.big_nums[0]

    def print_heaps(self):
        print(self.small_nums, 'len: ', len(self.small_nums))
        print(self.big_nums, 'len: ', len(self.big_nums))
        print("\n")
