class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        #intuition: completeHelp from neetcode youtube solution(https://www.youtube.com/watch?v=q6IEA26hvXc&t=1316s)
        #idea: find the left half of the imaginary combined array separately in nums1, nums2
        
        #run binary search on smaller array
        A,B=nums1,nums2
        if len(B) < len(A):
            A,B=B,A
        
        total=len(A)+len(B)
        half=total//2
        
        #binary search for middle on smaller array
        l,r=0,len(A)-1
        while True:
            i = (l+r)//2 #middle of A (smaller array)
            j = half-i-2 #middle of B (larger array)
            
            Aleft = A[i] if i>=0 else float("-infinity")
            Aright = A[i+1] if i+1<len(A) else float("infinity")
            Bleft = B[j] if j>=0 else float("-infinity")
            Bright = B[j+1] if j+1<len(B) else float("infinity")
            
            #partition correct case:
            if Aleft<=Bright and Aright>=Bleft:
                #odd
                if total%2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft)+ min(Aright, Bright))/2
            elif Aleft > Bright:
                r=i-1
            else:
                l=i+1
            
        