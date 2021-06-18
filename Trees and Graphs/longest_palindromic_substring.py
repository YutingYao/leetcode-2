"""
Longest Palindromic Substring:

Write a function that, given a string, returns its longest palindromic substring.
A palindrome is defined as a string that's written the same forward and backward. Note that single-character strings are palindromes.
You can assume that there will only be one longest palindromic substring.
"""


class Longest:
    def __init__(self, length, start_idx, end_idx):
        self.length = length
        self.start_idx = start_idx
        self.end_idx = end_idx


def longestPalindromicSubstring(string):
    longest = Longest(1, 0, 0)
    for idx in range(1, len(string)-1):

        checkPalindrome(string, longest,  1, idx-1, idx+1)  # odd
        checkPalindrome(string, longest, 0, idx, idx+1)  # even

    return string[longest.start_idx:longest.end_idx+1]


def checkPalindrome(string, longest, curr_len, nxt_left, nxt_right):

    # expand outwards
    while nxt_left >= 0 and nxt_right < len(string) \
            and string[nxt_left] == string[nxt_right]:
        curr_len += 2
        nxt_left -= 1
        nxt_right += 1

    if curr_len > longest.length:
        longest.length = curr_len
        longest.start_idx = nxt_left + 1
        longest.end_idx = nxt_right - 1


print(longestPalindromicSubstring("abaxyzzyxf"))
one = "abcba"
two = "abbazxzxabcba"
# print(checkPalindrome(one, 1, 1, 3))
# print(checkPalindrome(one, 0, 1, 3))
print(longestPalindromicSubstring(two))
print(longestPalindromicSubstring("sfd"))

"""
  
   [              spent   current
    [0,   2, 10],    _    0
    [3,   5,  0],   +10   10
    [9,  20,  6],   -6     4 
    [10, 12, 15],   -9    -5
    [10, 10,  8]     +7    2
   ]

   [              spent   current
    [0,   2, 10],    _    0
    [3,   5,  0],   +10   10
    [9,  20,  6],   -6     4 
    [10, 12, 15],   -9    -5
    [10, 10,  8],    +7    2
    [ 0,  0, 28],   -20    -18
    [ 0,  0, 0]     +28    10
   ]

      [              spent   current
    [0,   2, 10],    _    0
    [3,   5,  0],   +10   10
    [9,  20,  6],   -6     4 
    [10, 12, 15],   -9    -5
    [10, 10,  8],    +7    2
    [ 0,  0, 28],   -20    -18
    [ 0,  0, 0]     +28    10
   ]

"""
