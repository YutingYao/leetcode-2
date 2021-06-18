"""
Subsets II: Leetcode 90
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.

Example:

    Input: [1,2,2]

    Output:
        [
        [2],
        [1],
        [1,2,2],
        [2,2],
        [1,2],
        []
        ]
"""
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]

        if len(nums) < 1:
            return subsets
        nums.sort()

        # used to mark the idx where the non duplicate subsets started being added
        last_num_added_start = None
        for idx in range(len(nums)):
            subsets_length = len(subsets)

            # handle duplicates
            if idx > 0 and nums[idx] == nums[idx-1]:
                for index in range(last_num_added_start, subsets_length):
                    new_list = list(subsets[index])
                    new_list.append(nums[idx])
                    subsets.append(new_list)

            # non-duplicates
            else:
                for index in range(subsets_length):
                    new_list = list(subsets[index])
                    new_list.append(nums[idx])
                    subsets.append(new_list)

            last_num_added_start = subsets_length

        return subsets

# also available here: https://github.com/paulonteri/patterns-for-coding-questions/blob/master/Subsets/subsets_with_duplicates.py
