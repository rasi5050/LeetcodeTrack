class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        b = rec1[3]-rec1[1]
        (x1, y1) = (rec1[0], rec1[1]+b)
        (x2, y2) = (rec1[2], rec1[3])
        (x3, y3) = (rec1[2], rec1[3]-b)
        (x4, y4) = (rec1[0], rec1[1])
        
        b = rec2[3]-rec2[1]
        (a1,b1) = (rec2[0], rec2[1]+b)
        (a2,b2) = (rec2[2], rec2[3])
        (a3,b3) = (rec2[2], rec2[3]-b)
        (a4,b4) = (rec2[0], rec2[1])

        #edges overlap to right upper and left lower corners
        if (x4<a2 and y4<b2) and (a4<x2 and b4<y2):
            return True
        
        if (a4<x2 and b4<y2) and (x4<a2 and y4<b2):
            return True
        
        #edges overlap to left upper and right lower corners
        if (a3>x3 and b3<y1) and (x3>a1 and y3<b1):
            return True
        if (x3>a1 and y3<b1) and (a3>x1 and b3<y1):
            return True
        
        #one rectangle completely inside other
        if (x3>a3 and y3<b3) and (a1>x1 and b1<y1):
            return True
        
        if (a3>x3 and b3<y3) and (x1>a1 and y1<b1):
            return True
        
        #status: correct; intuition: find coordinates brute force all conditions and expand cases
        #Analysis: Time O(1); constant number of cases
        #Space O(1)
        #ref: 1/5/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day73/74,0.mastercardPsymetrics-x1pomo(5:30-6:00),1.rectangleOverlapTimed25Mins-x1pomo(6:00-6:30),2.implement-x2pomo(6:30-7:30),3.kClosestPointsToOriginTimed25Mins-x1pomo(7:30-8:00),4.implement-x2pomo(8:00-9:00),5.rectangleAreaTimed25Mins-x1pomo(9:00-9:30),6.implement-x2pomo(9:30-10:30),7.twoSumTimed25Mins-x1pomo(10:30-11:00),8.absorber-x1pomo(11:00-11:30)=x12pomo(5:30-11:30)
