class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        #idea: overlap area=shrink the 4 sides to minimum rectangle
        
        A, B, C, D = ax1, ay1, ax2, ay2
        E, F, G, H = bx1, by1, bx2, by2
        
        x1 = max(A, E)
        y1 = max(B, F)
        x2 = min(C, G)
        y2 = min(D, H)
        overlapArea = (x2-x1)*(y2-y1) if (x1<x2 and y1<y2) else 0   #checking overlap
        
        
        
        #total area = area of rect1 + area of rect2 - overlapArea (to avoid double counting of overlapping area, similar to A U B = A + B - (A intersection B))
        
        rect1Area = (ax2-ax1)*(ay2-ay1)
        rect2Area = (bx2-bx1)*(by2-by1)
        
        return (rect1Area+rect2Area)-overlapArea
    
        #status: correct
        #Analysis: Time O(1), Space O(1)
        #ref: 1/5/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day73/74,0.mastercardPsymetrics-x1pomo(5:30-6:00),1.rectangleOverlapTimed25Mins-x1pomo(6:00-6:30),2.implement-x2pomo(6:30-7:30),3.kClosestPointsToOriginTimed25Mins-x1pomo(7:30-8:00),4.implement-x2pomo(8:00-9:00),5.rectangleAreaTimed25Mins-x1pomo(9:00-9:30),6.implement-x2pomo(9:30-10:30),7.twoSumTimed25Mins-x1pomo(10:30-11:00),8.absorber-x1pomo(11:00-11:30)=x12pomo(5:30-11:30)

        
        