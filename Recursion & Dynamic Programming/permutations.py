"""
Permutations:

Write a function that takes in an array of unique integers
 and returns an array of all permutations of those integers in no particular order.
If the input array is empty, the function should return an empty array.
https://www.algoexpert.io/questions/Permutations
"""


# Upper Bound: O(n^2*n!) time | O(n*n!) space
# Roughly: O(n*n!) time | O(n*n!) space
def getPermutations(array):
    permutations = []
    if not array:
        return []
    getPermutationsHelper(array, [], permutations)
    return permutations


def getPermutationsHelper(array, curr, permutations):

    if not array:
        permutations.append(curr)
        # return

    for idx in range(len(array)):
        # array_copy = list(array)
        # curr_copy = list(curr)
        # curr_copy.append(array_copy.pop(idx))
        # getPermutationsHelper(array_copy, curr_copy, permutations)
        # # use slicing
        getPermutationsHelper(
            array[0:idx] + array[idx+1:],  # (new array) remove idx
            curr + [array[idx]],  # (new curr) add the number at idx
            permutations
        )


"""
Solution:

[1,2,3] <- array
        1,2,3 
        1,3,2 
        ​
        2,1,3
        2,3,1

        3,1,2
        3,2,1





		                           [1,2,3,4] <- array

	[1][2,3,4]           [2][1,3,4]         [3][1,2,4]                [4][1,2,3]

 [1,2] [1,3] [1,4]   [2,1] [2,3] [2,4]    [3,1] [3,2] [3,4]        [4,1] [4,2] [4,3] 

# explanatiion video at 18:00
O(n!.n.n) time 
n! -> number of permutations we have (number of leaves in recusrsive represantation)
n -> total of n*n calls to the factorial method
n -> removal from array ans creating permutations in the helper method (2n)
"""

print(getPermutations([1, 2]))
print(getPermutations([1, 2, 3]))
print(getPermutations([1, 2, 3, 4]))


def getPermutations2(array):
    all_permutations = []
    if array is None or len(array) < 1:
        return all_permutations

    getPermutationsHelper(array, all_permutations)
    return all_permutations


def getPermutationsHelper(array, all_permutations, idx=0):
    if idx == len(array) - 1:
        all_permutations.append(array[:])
        return

    for j in range(idx, len(array)):
        swap(array, idx, j)
        getPermutationsHelper(array, all_permutations, idx+1)
        swap(array, idx, j)


def swap(array, a, b):
    array[a], array[b] = array[b], array[a]
