"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        n = len(intervals)
        if n == 0:
            return 0
        
        intervals.sort(key=lambda x:x.end)

        max_heap = []
        
        for i in range(n-1,-1,-1):
            if max_heap and intervals[i].end <= (-1*max_heap[0]):
                heapq.heappop(max_heap)
            heapq.heappush(max_heap,-1*intervals[i].start)
            
        return len(max_heap)

        