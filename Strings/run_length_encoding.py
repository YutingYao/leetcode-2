"""
Run-Length Encoding:

Write a function that takes in a non-empty string and returns its run-length encoding.
From Wikipedia, "run-length encoding is a form of lossless data compression in which runs of data are stored as a single data value and count,
 rather than as the original run."
For this problem, a run of data is any sequence of consecutive, identical characters. So the run "AAA" would be run-length-encoded as "3A".
To make things more complicated, however, the input string can contain all sorts of special characters, including numbers.
And since encoded data must be decodable, this means that we can't naively run-length-encode long runs.
For example, the run "AAAAAAAAAAAA" (12 As), can't naively be encoded as "12A", since this string can be decoded as either "AAAAAAAAAAAA" or "1AA.
Thus, long runs (runs of 10 or more characters) should be encoded in a split fashion; the aforementioned run should be encoded as "9A3A".
https://www.algoexpert.io/questions/Run-Length%20Encoding
"""


# O(n) time | O(n) space - where n is the len of the string
def runLengthEncoding(string):
    encoded = []

    idx = 0
    while idx < len(string):

        count = 1
        while idx < len(string)-1 and string[idx] == string[idx+1]:
            count += 1
            idx += 1

        # add the count to output
        while count > 9:
            encoded.append('9')  # O(1) time
            encoded.append(string[idx])
            count -= 9
        encoded.append(str(count))
        encoded.append(string[idx])

        idx += 1

    return "".join(encoded)


"""
Sample Input
    string = "AAAAAAAAAAAAABBCCCCDD"
    "zAAABBBB222"
Sample Output
    "9A4A2B4C2D"
    "1z3A4B32"

"AAAAAAAAAAAAABBCCCCDD"
count for a = 13
- we'll have to make it less than 10: 9 and 4


# Input: non-empty string that can contain special characters and numbers
# Output: encoded string

# # Approach: 
# have and output
# iterate through each character having a starting count of 1
# while the next character is similar to the current, we move to the next and count += 1
# encode the character
    - while the count > 10: add 9char to the output & count -= 9
    - add countchar to the output
# move to next new character and repeat the process

"""
