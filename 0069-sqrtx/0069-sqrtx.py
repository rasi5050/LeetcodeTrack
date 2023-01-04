class Solution:
    def mySqrt(self, x: int) -> int:
        """TLE
        for i in range(x):
            if (i*i) <= x < (i+1)*(i+1):
                return i
        return x
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