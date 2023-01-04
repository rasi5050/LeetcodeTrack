class Solution:
    def mySqrt(self, x: int) -> int:
        """TLE
        for i in range(x):
            if (i*i) <= x < (i+1)*(i+1):
                return i
        return x
        """
        """
        #instead of going all the way minimize the work in a range
        t=x
        while t:
            t//=2
            if t*t<=x:
                break
        for i in range(t, x):
            if (i*i) <= x < (i+1)*(i+1):
                return i
        return x
        """
        #better idea; binary search from in 0 to x//2 range
        """working code; commented to try alternate method
        if x==1: return 1
        l=0
        r=x//2
        
        while l<=r:
            mid=(l+r)//2
            prod = mid*mid
            if prod == x:
                return mid
            elif prod>x:
                r=mid-1
            else:
                l=mid+1
        return r
        """
        if x==1: return 1
        l, r = 0, x//2
        while l<=r:
            mid = (l+r)//2
            prod = mid*mid
            prodNext = (mid+1)*(mid+1)
            if prod <= x < prodNext:
                return mid
            elif prod>x:
                r=mid-1
            else:
                l=mid+1
        #status: correct; idea from (https://leetcode.com/problems/sqrtx/discuss/25061/Python-binary-search-solution-(O(lgn)).)
        #Analysis: Time O(n logn); binary search
        #Space O(1)
        #ref: 1/4/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day72/72,1.integerToEnglishWordsTimed25Mins-x1pomo(14:00-14:30),2.implement-x2pomo(14:30-15:30),3.rectangleOverlapTimed25Mins-x1pomo(15:30-16:00),4.implement-x2pomo(16:00-17:00)=x6pomo(14:00-17:00)

        
            