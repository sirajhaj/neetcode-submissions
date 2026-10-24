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
        
        starts = sorted(intervals,key=lambda x:x.start)
        intervals.sort(key=lambda x:x.end)

        s,e,cnt = 0,0,0
        max_lap = 0
        
        while s<n and e<n:
            while s<n and starts[s].start < intervals[e].end :
                s+=1
                cnt+=1
            max_lap = max(max_lap,cnt)
            e+=1
            cnt-=1

        return max_lap

        