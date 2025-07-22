# Problem: Non-overlapping Intervals - https://leetcode.com/problems/non-overlapping-intervals/description/

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        inter=0
        intervals.sort(key=lambda x: x[1])
        n=len(intervals)
        prev=intervals[0][1]
        for i in range(1,n):
            if (prev>intervals[i][0]):
                inter+=1
            else:
                prev=intervals[i][1]
                
        return inter