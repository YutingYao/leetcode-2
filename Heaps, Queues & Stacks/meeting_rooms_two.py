"""
Meeting Rooms II: Leetcode 253

Given an array of meeting time intervals consisting of start and end times:
[[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
"""

# this can be optimized futher plus variables have been overused:
# this is to help in undertanding the solution
from typing import List
import heapq


# time O(n log(n)) | space O(n)
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        if not intervals:
            return 0

        # sort meetings by starting time
        intervals.sort(key=lambda x: x[0])

        # # Logic:
        # if the next meeting is earlier than the earliest ending time,
        # then no room will be free for it. Otherwise,
        # update the ending time (for the room)

        # # used to store the ending times of all meeting rooms
        # if a second meeting is held in a room, we replace the 1st's ending time,
        # we delete the 1st meeting ending time and add the 2nd's

        # create ending times heap
        # the heap will help us in keep the earliest ending time per room 'on top, [0]'
        ending_times = []
        heapq.heappush(ending_times, intervals[0][1])

        i = 1
        while i < len(intervals):
            # in any case, we will add the meeting's ending time to the ending_times,
            # however, if the earliest ending time is less than it's starting,
            # it means those two can share a room
            # so we remove the earlier one's ending time

            # # check if (curr starting time) overlaps earliest ending time
            earliest_ending_time = ending_times[0]
            curr_meeting = intervals[i]

            # cannot share room
            if curr_meeting[0] < earliest_ending_time:
                # similar to adding another meeting room
                heapq.heappush(ending_times, curr_meeting[1])
            # can share room
            # meeting starts later than the earliest ending
            # free room -> not overlap
            else:
                # remove the first room's ending time from the count
                # similar to updating meeting room's earliest ending
                heapq.heappop(ending_times)
                heapq.heappush(ending_times, curr_meeting[1])

            i += 1

        # we always added rooms to the heap and:
        # whenerver we found conflicts in times we did'nt remove from the heap but,
        # we removed when we were reusing the same room
        # the meeting ending times that were not replaced
        return len(ending_times)


"""
Input:
    [[0,30],[5,10],[15,20]]
    [[0,30]]
    [[0,30],[5,10],[1,20],[7,30],[50,10],[15,20],[0,30],[5,10],[15,20]]
Output:
    2
    1
    6
"""
