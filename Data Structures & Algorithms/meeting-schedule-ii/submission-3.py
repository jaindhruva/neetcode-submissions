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
        max_meetings = 0
        intervals.sort(key = lambda interval: interval.start)

        for meeting in intervals:
            while min_heap and min_heap[0] <= meeting.start:
                # end meetings that end before next one start
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, meeting.end)
            
            max_meetings = max(max_meetings, len(min_heap))

        return max_meetings
