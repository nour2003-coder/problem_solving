# Problem: My Calendar I - https://leetcode.com/problems/my-calendar-i/description/

import bisect
class MyCalendar:

    def __init__(self):
        self.calendar=[]


    def book(self, start: int, end: int) -> bool:
        booking=[start,end]
        index=bisect.bisect_left(self.calendar,booking)
        if (index<=0 or self.calendar[index-1][1]<=start) and (index>=len(self.calendar) or self.calendar[index][0]>=end):
            self.calendar.insert(index,[start,end])
            return(True)
        return(False)


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)