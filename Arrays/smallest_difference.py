"""
Smallest Difference:

Write a function that takes in two non-empty arrays of integers,
 finds the pair of numbers (one from each array) whose absolute difference is closest to zero,
 and returns an array containing these two numbers, with the number from the first array in the first position.

Note that the absolute difference of two integers is the distance between them on the real number line. 
For example, the absolute difference of -5 and 5 is 10, and the absolute difference of -5 and -4 is 1.

You can assume that there will only be one pair of numbers with the smallest difference.
"""


def smallestDifference1(arrayOne, arrayTwo):

    smallest = float('inf')
    smallest_nums = []

    for num_one in arrayOne:
        for num_two in arrayTwo:

            abs_diff = abs(num_one-num_two)
            if abs_diff < smallest:
                smallest = abs_diff
                smallest_nums = [num_one, num_two]

    return smallest_nums


# Start by sorting both arrays.
# Put a pointer at the beginning of both arrays and evaluate the absolute difference of the pointer-numbers.
# If the difference is equal to zero, then you've found the closest pair;
#  otherwise, increment the pointer of the smaller of the two numbers to find a potentially better pair.
# Continue until you get a pair with a difference of zero or until one of the pointers gets out of range of its array.

# O(nlog(n) + mlog(m)) time | O(1) space
def smallestDifference(arrayOne, arrayTwo):

    arrayOne.sort()
    arrayTwo.sort()

    smallest = float('inf')
    smallest_nums = None

    pointer_one = 0
    pointer_two = 0
    while pointer_one < len(arrayOne) and pointer_two < len(arrayTwo):

        # check if we have found a smaller absolute difference
        abs_diff = abs(arrayOne[pointer_one] - arrayTwo[pointer_two])
        if abs_diff < smallest:
            # if we find 0, this will be the smallest difference we can find
            if abs_diff == 0:
                return [arrayOne[pointer_one], arrayTwo[pointer_two]]

            smallest = abs_diff
            smallest_nums = [arrayOne[pointer_one], arrayTwo[pointer_two]]

        # try to reduce the absolute difference
        if arrayOne[pointer_one] < arrayTwo[pointer_two]:
            pointer_one += 1
        else:
            pointer_two += 1

    return smallest_nums


# O(nlog(n) + mlog(m)) time | O(1) space
def smallestDifference3(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()

    smallest_nums = [arrayOne[0], arrayTwo[0]]

    one = 0
    two = 0
    while one < len(arrayOne) and two < len(arrayTwo):

        curr_smallest = abs(smallest_nums[0] - smallest_nums[1])
        curr_diff = abs(arrayOne[one] - arrayTwo[two])

        # update smallest_nums
        if curr_diff < curr_smallest:
            smallest_nums = [arrayOne[one], arrayTwo[two]]

        # check if we should move one forward
        # if one is less than two, we should try to increment it
        if arrayOne[one] < arrayTwo[two]:
            one += 1
        else:
            two += 1

    return smallest_nums


# O(nlog(n) + mlog(m)) time | O(1) space
def smallestDifference4(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()

    smallest_nums = [arrayOne[0], arrayTwo[0]]

    one = 0
    two = 0
    while one < len(arrayOne) and two < len(arrayTwo):

        curr_smallest = abs(smallest_nums[0] - smallest_nums[1])
        curr_diff = abs(arrayOne[one] - arrayTwo[two])

        # update smallest_nums
        if curr_diff < curr_smallest:
            smallest_nums = [arrayOne[one], arrayTwo[two]]

        is_two_not_at_end = two < len(arrayTwo) - 1
        is_one_at_end = one == len(arrayOne) - 1
        # check if we should move two forward
        if is_two_not_at_end and (is_one_at_end or
                                  (abs(arrayOne[one] - arrayTwo[two+1]) < abs(arrayOne[one+1] - arrayTwo[two]))):  # moving two forward will create a smaller absolute diff
            two += 1

        # check if we should move one forward
        else:
            one += 1
    return smallest_nums
