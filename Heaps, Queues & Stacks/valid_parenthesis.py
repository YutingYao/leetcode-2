"""
Valid Parentheses: Leetcode 20 / Balanced Brackets

https://www.algoexpert.io/questions/Balanced%20Brackets
"""


class Solution(object):
    # O(n) time | O(n) space
    def isValid(self, s):

        myStack = []
        count = 0  # keep track of number of elements

        # used to find closing brackets
        match = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        for par in s:
            # handle opening brackets
            if par == "(" or par == "{" or par == "[":
                myStack.append(par)
                count += 1

            # handle closing brackets
            else:
                # check if we can find the corresponding opening bracket
                if count < 1 or match[myStack.pop()] != par:
                    return False
                # the pop() above removed a alement from the stack
                count -= 1

        # return true if stack is empty(all matched successfully)
        return count == 0


class SimplerSolution(object):
    def isValid(self, s):

        myStack = []

        match = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        for par in s:
            if par == "(" or par == "{" or par == "[":
                myStack.append(par)

            elif len(myStack) == 0 or match[myStack.pop()] != par:
                return False

        return len(myStack) == 0


def balancedBrackets(string):
    opening_brackets = "([{"
    matching_brackets = {")": "(", "]": "[", "}": "{"}
    stack = []
    for char in string:

        if char not in matching_brackets and char in opening_brackets:  # opening bracket
            stack.append(char)

        # closing brackets
        elif char in matching_brackets and(not stack or matching_brackets[char] != stack.pop(-1)):
            return False

    return len(stack) == 0


print(balancedBrackets("([])(){}(())()()"))
print(balancedBrackets("([])(){}(()))()()"))
