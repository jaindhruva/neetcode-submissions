"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        min_heap = []
        meetings_running = 0
        max_meetings = 0
        intervals.sort(key = lambda interval: interval.start)

        for i in range(len(intervals)):
            meeting = intervals[i]

            if meetings_running == 0:
                # just add to minheap and proceed to next
                heapq.heappush(min_heap, meeting.end)
                meetings_running += 1
            else:
                while min_heap and min_heap[0] <= meeting.start:
                    # end meetings that end before next one start
                    heapq.heappop(min_heap)
                    meetings_running -= 1
                heapq.heappush(min_heap, meeting.end)
                meetings_running += 1


            max_meetings = max(max_meetings, meetings_running)

        return max_meetings
