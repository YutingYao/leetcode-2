"""
Best Time to Buy and Sell Stock

Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock),
 design an algorithm to find the maximum profit.
Note that you cannot sell a stock before you buy one.

Example 1:
    Input: [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
                Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:
    Input: [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transaction is done, i.e. max profit = 0.
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""


class Solution:
    def maxProfit(self, array):
        # will add base cases
        if not array or len(array) == 1:
            return 0
        if len(array) == 2:
            if array[1] - array[0] > 0:
                return array[1] - array[0]
            return 0

          # Hello

        max_profit = 0

        left = len(array) - 2
        right = len(array) - 1

        while left >= 0:

            if left != len(array) - 2:
                # check whether we will replace right with the prev left
                if array[left+1] > array[right]:
                    right = left + 1

            max_profit = max(max_profit, (array[right] - array[left]))

            left -= 1

        return max_profit
