# didn't solve it using dynamic programming though 😭😭😭
"""
Longest Palindromic Substring: Leetcode 5

Given a string s, return the longest palindromic substring in s.
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:

        length = len(s)

        if length <= 1:
            return s

        longest_pal_left = 0
        longest_pal_right = 0
        i = 0
        while i < length:

            # check for both even and odd palindromes
            # Examples: even -> zyaaaagh, odd -> zyaaagh
            odd_pal_checker = self.expandFromMiddle(s, i, i)
            even_pal_checker = 0
            if (i + 1) < length:
                even_pal_checker = self.expandFromMiddle(s, i, i + 1)

            # record the largest palindrome we found from the expandFromMiddle

            # odd is longer
            if odd_pal_checker > even_pal_checker:
                # if longer than the current longest palindrome
                if odd_pal_checker > (longest_pal_right - longest_pal_left) + 1:
                    # record odd
                    longest_pal_left = i - (odd_pal_checker // 2)
                    longest_pal_right = i + (odd_pal_checker // 2)

            # even is longer
            else:
                # if longer than the current longest palindrome
                if even_pal_checker > (longest_pal_right - longest_pal_left) + 1:
                    # record even
                    # using modulus so as to get integers (not float)
                    longest_pal_left = i - ((even_pal_checker // 2) - 1)
                    longest_pal_right = i + (even_pal_checker // 2)
            #
            i += 1

        #
        return s[longest_pal_left: longest_pal_right+1]

    def expandFromMiddle(self, s, left, right):

        if s[left] != s[right]:
            return 0

        # pointers showing how far we have expanded (which marks how wide the palindrome is)
        exp_left = left
        exp_right = right

        while left >= 0 and right < len(s) and s[left] == s[right]:
            # expand
            exp_left = left
            exp_right = right

            # move on to checking the next
            left -= 1
            right += 1

        # return len of the longest palindrome we found
        return (exp_right - exp_left) + 1


"""
Example:

Input:
    "babad"
    "caba"
    "abacdfgdcaba"
    "cbbd"
    "a"


Output:
    "bab"
    "aba"
    "aba"
    "bb"
    "a"
"""


def RunTest():
    tests = [
        "bb"
        "babad",
        "coca",
        "caba",
        "abacdfgdcaba",
        "cbbd",
        "a",
        ""]
    sol = Solution()

    for i in tests:
        print(sol.expandFromMiddle(i))


RunTest()
