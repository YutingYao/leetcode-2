"""
Max Substring Alphabetically
Given a string, determine the maximum alphabetically, substring
"""


def maxSubstring(s):

    if len(s) < 1:
        return ""

    # get all characters' indexes
    # sort characters alphabetically
    characters = []
    idx_store = {}
    for idx, char in enumerate(s):
        if char not in idx_store:
            characters.append(char)
            idx_store[char] = [idx]
        else:
            char_indexes = idx_store[char]
            char_indexes.append(idx)
            idx_store[char] = char_indexes

    characters.sort()
    # handle the last character's (from characters array) substrings only
    last_char = characters[-1]

    # get all substrings starting with the last character
    # sort them
    substrings = []
    for idx in idx_store[last_char]:
        right = idx
        while right < len(s):
            substrings.append(s[idx:right+1])
            right += 1

    substrings.sort()
    return substrings[-1]


print(maxSubstring("apple"))
print(maxSubstring("apsgsxvbbdbsdbsdknnple"))
print(maxSubstring("asazsxs"))

# Not on Leetcode
