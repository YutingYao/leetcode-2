"""
Climbing Stairs / Triple Step:

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
https://leetcode.com/problems/climbing-stairs/
"""


class Solution:
    def climbStairs(self, n):
        return self.helper(n)

    # in case we reach remaining=0, then we have found way (a correct set of steps)
    def helper(self, remaining, store={0: 1}):  # store={0:1} is a base case
        if remaining < 0:
            return 0

        if remaining in store:
            return store[remaining]

        total = self.helper(remaining-1, store) + \
            self.helper(remaining-2, store)

        store[remaining] = total

        return store[remaining]
