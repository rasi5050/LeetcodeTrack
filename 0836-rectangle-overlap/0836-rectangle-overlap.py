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

        if (x4<a2 and y4<b2) and (a4<x2 and b4<y2):
            return True
        if (a4<x2 and b4<y2) and (x4<a2 and y4<b2):
            return True
        
        if (a3>x3 and b3<y1) and (x3>a1 and y3<b1):
            return True
        if (x3>a1 and y3<b1) and (a3>x1 and b3<y1):
            return True
        
        #one rectangle inside other
        if (x3>a3 and y3<b3) and (a1>x1 and b1<y1):
            return True
        
        if (a3>x3 and b3<y3) and (x1>a1 and y1<b1):
            return True
        
