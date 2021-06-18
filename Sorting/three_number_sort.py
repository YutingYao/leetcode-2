"""
Three Number Sort:

You're given an array of integers and another array of three distinct integers.
The first array is guaranteed to only contain integers that are in the second array, and the second array represents a desired order for the integers in the first array.
For example, a second array of [x, y, z] represents a desired order of [x, x, ..., x, y, y, ..., y, z, z, ..., z] in the first array.
Write a function that sorts the first array according to the desired order in the second array.
The function should perform this in place (i.e., it should mutate the input array), and it shouldn't use any auxiliary space (i.e., it should run with constant space: O(1) space).
Note that the desired order won't necessarily be ascending or descending and that the first array won't necessarily contain all three integers found in the second array—it might only contain one or two
"""


# divide array into three arrays (in place) and
#  move values order[0] into the first and values order[1] into the third

# O(n) time | O(1) space
def threeNumberSort(array, order):

    first_array_next = 0
    third_array_next = len(array) - 1

    idx = 0
    # while idx < len(array):
    while idx <= third_array_next:

        # add to first array
        if array[idx] == order[0] and idx > first_array_next:
            swap(array, idx, first_array_next)
            first_array_next += 1  # increase first array size

        # add to third array
        elif array[idx] == order[2] and idx < third_array_next:
            swap(array, idx, third_array_next)
            third_array_next -= 1  # increase third array size

        else:
            idx += 1

    return array


def swap(array, idx_one, idx_two):
    array[idx_one], array[idx_two] = array[idx_two], array[idx_one]


# O(n) time | O(1) space - where n is the length of the array
# Bucket sort
def threeNumberSort(array, order):

    valueCounts = [0, 0, 0]

    for element in array:
        orderIdx = order.index(element)
        valueCounts[orderIdx] += 1

    for i in range(3):
        value = order[i]
        count = valueCounts[i]
        numElementsBefore = sum(valueCounts[:i])
        for n in range(count):
            currentIdx = numElementsBefore + n
            array[currentIdx] = value
    return array
