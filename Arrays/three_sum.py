"""
Three Sum. (3Sum)

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

The solution set must not contain duplicate triplets.
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()  # will make spoting of duplicates easy

        triplets = []
        length = len(nums)

        for i in range(length-2):  # ignore last two

            # check if element is a duplicate. the first cannot be a duplicate
            if i > 0 and nums[i] == nums[i-1]:
                # skip handling an element if it's similar to the one before it
                # because it is sorted, we effectively skip duplicates
                continue

            # TWO SUM for a sorted array
            # 1. find elements that will add up to 0
            # 2. check inner elements
            left = i + 1
            right = length - 1
            while left < right:

                # will be used to check if the sum is equal to 0
                total = nums[i] + nums[left] + nums[right]

                # if total is less than 0 we try to increase it's value
                if total < 0:
                    left += 1  # moving left to a lerger value

                # if total is more than 0 we try to decrease it's value
                elif total > 0:
                    right -= 1  # moving right to a smaller value

                # 1. add list of elements to triplets
                # 2. check inner elements
                else:
                    # add elements to triplets
                    triplets.append([nums[i], nums[left], nums[right]])

                    # check inner elements
                    # 1. skip similar elements
                    # 2. move to inner elements

                    # skip:
                    # no need to continue with an element with the same value as l/r
                    # Skip all similar to the current left and right so that,
                    # when we are moving to the next element, we dont move to an element with the same value
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1

                    # move to inner elements
                    left += 1
                    right -= 1

        return triplets


# O(n^2) time | O(n) space - where n is the length of the input array
def threeNumberSum(array, targetSum):
    triplets = []
    # help prevent duplicates and the result in triplets [] will be sorted
    array.sort()
    length = len(array)

    for idx, num in enumerate(array):

        # two sum
        left = idx + 1
        right = length - 1
        while left < right and right < length:
            total = num + array[left] + array[right]

            if total == targetSum:
                triplets.append([num, array[left], array[right]])
                right -= 1
                left += 1
            elif total > targetSum:
                right -= 1
            else:
                left += 1
    return triplets


"""
Example 1:
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]

Example 2:
    Input: nums = []
    Output: []

Example 3:
    Input: nums = [0]
    Output: []
"""
threeNumberSum([1, 2, 3, 4], 6)
