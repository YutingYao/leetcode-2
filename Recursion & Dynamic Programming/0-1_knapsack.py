"""
Knapsack Problem:

You're given an array of arrays where each subarray holds two integer values and represents an item;
 the first integer is the item's value, and the second integer is the item's weight.
You're also given an integer representing the maximum capacity of a knapsack that you have.
Your goal is to fit items in your knapsack without having the sum of their weights exceed the knapsack's capacity,
 all the while maximizing their combined value. Note that you only have one of each item at your disposal.
Write a function that returns the maximized combined value of the items that you should pick as well as an array of the indices of each item picked.
If there are multiple combinations of items that maximize the total value in the knapsack, your function can return any of them.
https://www.algoexpert.io/questions/Knapsack%20Problem
"""


# O(2^n) time | O(n) space
def knapsackProblem(items, capacity, idx=0, added=[]):
    if idx >= len(items):
        return [0, added]

    curr_weight = items[idx][1]
    curr_value = items[idx][0]

    if curr_weight > capacity:
        result = knapsackProblem(items, capacity, idx+1, added)  # skip current
    else:
        # add current to knapsack
        not_skip = knapsackProblem(
            items, capacity-curr_weight, idx+1, added + [idx])
        not_skip[0] = curr_value + not_skip[0]

        skip = knapsackProblem(items, capacity, idx+1, added)  # skip current

        if skip[0] > not_skip[0]:
            result = skip
        else:
            result = not_skip

    return result
