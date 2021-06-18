"""
Maximum Subarray:

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
"""


# O(n) time | O(1) space
class Solution:
    def maxSubArray(self, nums):
        # # # find the maximum subarray per given element:
        # # check which one is larger:
        # # adding the element to the current subarray or starting a new subarray at the element

        # the max subarray we found's sum
        max_sum = float("-inf")

        # sum of the current subarray that we are working with
        curr_subarray = float("-inf")
        for num in nums:
            # result of adding the element to the current subarray
            after_add = curr_subarray + num

            # check if adding the num to the current subarray will be
            # a longer sum than starting a new subarray at the element
            # then the current subarray should be the longer/larger of the two
            if after_add > num:
                curr_subarray = after_add
            else:
                curr_subarray = num

            # record the largest (sum) we found
            if curr_subarray > max_sum:
                max_sum = curr_subarray

        return max_sum
