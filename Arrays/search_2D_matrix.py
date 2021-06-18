"""
Search a 2D Matrix:

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
https://leetcode.com/problems/search-a-2d-matrix/
"""


from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int):

        row = 0
        while row < len(matrix):

            # # check rows
            # check last item in row
            if matrix[row][len(matrix[0])-1] < target:  # move to next row
                row += 1
            elif matrix[row][0] > target:
                return False

            # # found correct row
            # Binary Search on Row
            else:
                left = 0
                right = len(matrix[0])-1
                while left <= right:

                    mid = (right + left) // 2

                    if matrix[row][mid] == target:
                        return True

                    if matrix[row][mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1

                return False

        return False
