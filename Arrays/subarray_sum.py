"""
Subarray Sum

Given an array of integers and an integer k,
you need to find the total number of continuous subarrays whose sum equals to k.
"""


# O(n) time | O(n) space | n = len(array)
class Solution:
    # check if a total sum in the past plus the current will be equal to k
    # if a (the current sum - a previous sum = k),
    # then elements in the array between must add up to k
    def subarraySum(self, nums: List[int], k: int) -> int:

        curr_sum = 0
        total = 0
        # the store has to have 0 to deal with the case where k is in the list
        store = {0: 1}

        # if (the current sum - a sum in the past = k),
        # then the subarray in between them adds up to k
        for num in nums:
            # curr_sum - k = the requred past sum
            curr_sum += num
            needed_diff = curr_sum - k

            # check for the needed_diff
            if needed_diff in store:
                # we add   the number of possible times we can get that needed_diff
                total += store[needed_diff]

            # add the current sum to the store
            if curr_sum in store:
                store[curr_sum] = store[curr_sum] + 1
            else:
                store[curr_sum] = 1

        return total


"""
Example Testcase:

Input:nums = [1,1,1], k = 2
Output: 2
"""
