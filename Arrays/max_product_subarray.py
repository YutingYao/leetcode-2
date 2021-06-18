"""
Maximum Product Subarray:

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:
    Input: [2,3,-2,4]
    Output: 6
    Explanation: [2,3] has the largest product 6.
Example 2:
    Input: [-2,0,-1]
    Output: 0
    Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""


# O(n) time | O(1) space
class Solution:
    def maxProduct(self, array):

        if not array:
            return -1

        max_product = curr_max = curr_min = array[0]

        for idx in range(1, len(array)):

            temp_curr_max = curr_max
            curr_max = max(
                curr_max * array[idx],
                curr_min * array[idx],  # if array[idx] is negative [-2, 3, -4]
                array[idx]  # helps if array[idx-1] is 0 eg: [0, 2]
            )
            curr_min = min(
                temp_curr_max * array[idx],
                curr_min * array[idx],
                array[idx]
            )

            max_product = max(max_product, curr_max)

        return max_product


sol = Solution()
print(sol.maxProduct([2, 2, 2, 1, -1, 5, 5]))
print(sol.maxProduct([-2, 3, -4]))
print(sol.maxProduct([2]))
print(sol.maxProduct([]))
print(sol.maxProduct([-5]))
print(sol.maxProduct([0, 2, 2, 2, 1, -1, -5, -5]))
print(sol.maxProduct([0, 2]))
