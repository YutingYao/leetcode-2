"""
Staircase Traversal:
You're given two positive integers representing the height of a staircase and the maximum number of steps that you can advance up the staircase at a time.
Write a function that returns the number of ways in which you can climb the staircase.

For example, if you were given a staircase of height = 3 and maxSteps = 2 you could climb the staircase in 3 ways.
You could take 1 step, 1 step, then 1 step, you could also take 1 step, then 2 steps, and you could take 2 steps, then 1 step.

Note that maxSteps <= height will always be true.

Sample Input:
    height = 4
    maxSteps = 2
Sample Output:
    5
    // You can climb the staircase in the following ways: 
    // 1, 1, 1, 1
    // 1, 1, 2
    // 1, 2, 1
    // 2, 1, 1
    // 2, 2
    
https://www.algoexpert.io/questions/Staircase%20Traversal
"""


# 0(k^n) time, 0(n) space - where k is the max steps, n - number of steps
def staircaseTraversal00(height, maxSteps):
    return staircaseTraversalHelper00(height, maxSteps)


def staircaseTraversalHelper00(height_remaining, max_steps):

    if height_remaining == 0:
        # if are exactly at the last step, we have found a way
        return 1
    elif height_remaining < 0:
        # if we pass the last step, we made a mistake
        return 0

    ways = 0
    for step in range(1, max_steps+1):
        ways += staircaseTraversalHelper00(height_remaining - step, max_steps)

    return ways


# memoization:
# 0(k*n) time, 0(n) space - where k is the max steps, n - number of steps
# for each call, we'll have to sum k elements together
# for each of our n recursive calls, we have to do k work
def staircaseTraversal(height, maxSteps):
    return staircaseTraversalHelper(height, maxSteps, {0: 1})


def staircaseTraversalHelper(height_remaining, max_steps, store):

    if height_remaining < 0:
        # if we pass the last step, we made a mistake
        return 0

    # memoize
    if height_remaining in store:
        return store[height_remaining]

    ways = 0
    for step in range(1, max_steps+1):
        ways += staircaseTraversalHelper(height_remaining - step,
                                         max_steps, store)

    store[height_remaining] = ways  # memoize

    return store[height_remaining]


# 0(k*n) time, 0(n) space - where k is the max steps, n - number of steps
def staircaseTraversalIter(height, maxSteps):
    ways = [0] * (height + 1)
    ways[0] = 1  # there are 1 ways to reach at step 0

    for curr_height in range(1, height+1):
        steps = 0

        curr = curr_height - 1
        counter = maxSteps
        while curr >= 0 and counter > 0:
            steps += ways[curr]
            curr -= 1
            counter -= 1

        ways[curr_height] = steps
    return ways[height]


# TODO: Sliding window
