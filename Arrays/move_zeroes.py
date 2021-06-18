"""
Move Zeroes

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note:
    You must do this in-place without making a copy of the array.
    Minimize the total number of operations.
"""


# 0(n) time | 0(1) space
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        length = len(nums)

        # will mark the next char to be replaced
        anchor = 0

        # reorder list skipping all zeros (The first one might be replaced by itself if it's not 0)
        for i in range(length):

            # replace
            # if the current char is 0 it will not replace the prev
            if nums[i] != 0:
                nums[anchor] = nums[i]
                anchor += 1

        # from where the anchor last stuck,
        # replace all the nums from the anchor to the end with 0
        while anchor < length:
            nums[anchor] = 0
            anchor += 1
