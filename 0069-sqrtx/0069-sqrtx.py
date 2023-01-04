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
            