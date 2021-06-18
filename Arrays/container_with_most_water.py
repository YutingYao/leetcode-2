"""
Container With Most Water:

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0).
Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
Notice that you may not slant the container.
https://leetcode.com/problems/container-with-most-water/
"""


class SolutionBF:
    def maxArea(self, height):

        max_area = 0

        for idx in range(len(height)):

            for idx_two in range(idx+1, len(height)):

                h = min(height[idx], height[idx_two])
                w = idx_two - idx

                max_area = max(max_area, w*h)

        return max_area


class Solution:
    def maxArea(self, height):

        max_area = 0
        left, right = 0, len(height) - 1
        while left < right:

            # calculate area
            h = min(height[left], height[right])
            w = right - left
            max_area = max(max_area, h*w)

            # move pointer
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return max_area
