class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #intuition: complete help from neetcode youtube video(https://www.youtube.com/watch?v=q6IEA26hvXc)
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2
        
        if len(B) < len(A):
            A, B = B, A
        l, r = 0, len(A) - 1
        
        while True:
            i = (l+r)//2
            j = half - i - 2
            
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")
            
            if Aleft <= Bright and Bleft <= Aright:
                if total %2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright))/2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
                    
        #status: success; complete help from neetcode
        # ref:11/4/2022P2:rack1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day32/32:do,1.findMinInRotatedSortedArrayTimed25Mins-x1pomo(6:30-7:00),2.implement-x2pomo(7:00-8:00),3.medianOfTwoSortedArrayTimed25Mins-x1pomo(8:00-8:30),4.implement-x2pomo(8:30-9:30),5.matrixTimed25Mins-x1pomo(9:30-10:00),6.implement-x2pomo(10:00-11:00),7.absorber-x1pomo(11:00-11:30)=x10pomo(6:30-11:30)

            