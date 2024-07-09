class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        endTime = -1
        for start, end in intervals:
            if start < endTime:
                return False
            endTime = end
        return True