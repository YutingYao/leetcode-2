"""
Permutations: Leetcode 46

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
    Input: nums = [1,2,3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""


from typing import List


class Solution:
    def getPermutations(self, nums, num):
        array_of_nums = []
        for idx in range(len(nums) + 1):
            new_arr = list(nums)
            new_arr.insert(idx, num)
            array_of_nums.append(new_arr)
        return array_of_nums

    def permute(self, nums: List[int]):
        result = []
        result.append([nums[0]])
        index = 1
        while index < len(nums):
            num = nums[index]

            new_result = []
            for arr in result:
                new_result += self.getPermutations(arr, num)

            result = new_result

            index += 1

        return result


class Solution2:

    def combiner(self, num, arrays):
        for arr in arrays:
            arr.insert(0, num)
        return arrays

    def permute(self, nums):

        if len(nums) == 0:
            return []

        elif len(nums) == 1:  # recursion base case
            return [nums]

        generated = []  # store all generated permutations

        # get premutations with the number at nums[idx] at the front of the list (index 0)
        for idx in range(len(nums)):

            # remove nums[idx] from the list
            new_nums = list(nums)
            temp = new_nums.pop(idx)

            # place nums[idx] at the front of each permutation(list), index 0
            combined = self.combiner(temp, self.permute(new_nums))

            generated += combined

        return generated
