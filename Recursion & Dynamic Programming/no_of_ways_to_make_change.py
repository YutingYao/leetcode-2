"""
Number Of Ways To Make Change:

Given an array of distinct positive integers representing coin denominations and
 a single non-negative integer n representing a target amount of money,
  write a function that returns the number of ways to make change for that target amount using the given coin denominations.
Note that an unlimited amount of coins is at your disposal.
https://www.algoexpert.io/questions/Number%20Of%20Ways%20To%20Make%20Change
"""


def numberOfWaysToMakeChange(n, denoms):
    # Write your code here.
    denoms.sort()
    return helper(n, denoms)


def helper(n, denoms):

    array = list(range(1, n+1))

    for idx in range(len(array)):
        times = 0
        for denom in denoms:
            if denom <= idx:
                times += 1
            else:
                break
        array[idx] = times
