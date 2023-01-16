# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        
        #something to do with binary search
        left=1
        right=n
        while left<=right:
            mid=(left+right)//2
            fnCall=isBadVersion(mid)
            fnCallPrev=isBadVersion(mid-1)
            if fnCallPrev==False and fnCall==True:
                return mid
            elif fnCall==False:
                left=mid+1
            else:
                right=mid-1