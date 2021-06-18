"""
Youngest Common Ancestor:

You're given three inputs, all of which are instances of an AncestralTree class that have an ancestor property pointing to their youngest ancestor.
The first input is the top ancestor in an ancestral tree (i.e., the only instance that has no ancestor--its ancestor property points to None / null),
 and the other two inputs are descendants in the ancestral tree.
Write a function that returns the youngest common ancestor to the two descendants.
Note that a descendant is considered its own ancestor.
So in the simple ancestral tree below, the youngest common ancestor to nodes A and B is node A.
https://www.algoexpert.io/questions/Youngest%20Common%20Ancestor
"""


# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


# 0(d) time | 0(d) space - where d is the depth (height) of the ancestral tree
def getYoungestCommonAncestor1(topAncestor, descendantOne, descendantTwo):

    store_one = {}
    store_two = {}
    while descendantOne != topAncestor or descendantTwo != topAncestor:
        # one
        if descendantOne != topAncestor:
            if descendantOne.name in store_two:  # if seen by other descendant
                return descendantOne
            else:  # keep track of visited
                store_one[descendantOne.name] = True
            descendantOne = descendantOne.ancestor  # move up

        # two
        if descendantTwo != topAncestor:
            if descendantTwo.name in store_one:  # if seen by other descendant
                return descendantTwo
            else:  # keep track of visited
                store_two[descendantTwo.name] = True
            descendantTwo = descendantTwo.ancestor  # move up

    return topAncestor  # will always be an ancestor


# 0(d) time | 0(1) space
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):

    dist_top_one = 0
    dist_top_two = 0
    curr_one = descendantOne
    curr_two = descendantTwo
    while curr_one != topAncestor or curr_two != topAncestor:  # calculate the distace to top ancestor
        if curr_one != topAncestor:
            dist_top_one += 1
            curr_one = curr_one.ancestor
        if curr_two != topAncestor:
            dist_top_two += 1
            curr_two = curr_two.ancestor

    while dist_top_one != dist_top_two:  # move the lower pointer upwards
        if dist_top_one > dist_top_two:
            dist_top_one -= 1
            descendantOne = descendantOne.ancestor
        else:
            dist_top_two -= 1
            descendantTwo = descendantTwo.ancestor

    while descendantOne != topAncestor or descendantTwo != topAncestor:
        if descendantTwo == descendantOne:
            return descendantOne

        descendantOne = descendantOne.ancestor
        descendantTwo = descendantTwo.ancestor

    return topAncestor  # will always be an ancestor


"""
Sample Input
// The nodes are from the ancestral tree below.
    topAncestor = node A
    descendantOne = node E
    descendantTwo = node I
            A
        /     \
       B       C
     /  \     /  \
    D     E F     G
 /   \
 H     I
Sample Output
    node B

Solution:
1. try to get the (pointers to the) nodes to be at the same level
    - for example pointer two should move up to D
    - this can be done by calculating the distace to the top ancestor,
        then moving the lower pointer upwards
2. iterate upwards and return when they are at the same node

"""


# 0(d) time | 0(1) space - where d is the depth (height) of the ancestral tree
def getYoungestCommonAncestor2(topAncestor, descendantOne, descendantTwo):

    # calculate height from top
    temp_one = descendantOne
    temp_two = descendantTwo
    one_count = two_count = 0
    while temp_one != topAncestor or temp_two != topAncestor:
        if temp_one != topAncestor:
            temp_one = temp_one.ancestor
            one_count += 1
        if temp_two != topAncestor:
            temp_two = temp_two.ancestor
            two_count += 1

    # level nodes
    while one_count != two_count:
        if one_count > two_count:
            descendantOne = descendantOne.ancestor
            one_count -= 1
        else:
            descendantTwo = descendantTwo.ancestor
            two_count -= 1

    # find common ancestor
    while True:
        if descendantOne == descendantTwo:
            return descendantOne

        descendantOne = descendantOne.ancestor
        descendantTwo = descendantTwo.ancestor
