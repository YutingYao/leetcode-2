"""
Sort Characters By Frequency: Leetcode 451

Given a string, sort it in decreasing order based on the frequency of characters.
"""


class Solution:
    def frequencySort(self, s: str) -> str:

        if not s:
            return ""

        store = {}

        # count occurences of each character
        for char in s:
            if char in store:
                store[char] = 1 + store[char]
            else:
                store[char] = 1

        # store dictionary keys sorted by the number of occurences
        sorted_chars_list = sorted(store, key=lambda x: store[x], reverse=True)

        # rebuild string
        str_temp = []
        for char in sorted_chars_list:
            str_temp.append(char * store[char])

        return "".join(str_temp)


"""
Input:
    "tree"
    "cccaaa"
    "Aabb"
    ""
Output:
    "eetr"
    "cccaaa"
    "bbAa"
    ""
"""
