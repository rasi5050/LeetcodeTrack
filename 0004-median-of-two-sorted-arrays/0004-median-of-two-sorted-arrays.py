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
                
        #status: correct
        #analysis: O(log(min(m, n))) #since binary search is applied on array of smaller length
        #ref: 11/18/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day41/42:(P1:doPaypalLeetcodeQuestion2/5(https://github.com/hxu296/leetcode-company-wise-problems-2022/blob/main/companies/Paypal.csv),do,1.medianOfTwoSortedArraysTimed25Mins-x1pomo(5:30-6:00),2.implement-x2pomo(6:00-7:00),3.zigzagConversionTimed25Mins-x1pomo(7:00-7:30),4.implement-x2pomo(7:30-8:30),5.trappingRainWaterTimed25Mins-x1pomo(8:30-9:00),6.implement-x2pomo(9:00-10:00),7.absorber-x1pomo(10:00-10:30)=x10pomo(5:30-10:30)==>11/18/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day41/42:(P1:doPaypalLeetcodeQuestion2/5(https://github.com/hxu296/leetcode-company-wise-problems-2022/blob/main/companies/Paypal.csv),do,1.mergeTwoSortedArrays-implement-x2pomo(7:00-8:00),2.zigzagConversionTimed25Mins-x1pomo(8:00-8:30),3.implement-x2pomo(8:30-9:30),4.trappingRainWaterTimed25Mins-x1pomo(9:30-10:00),6.implement-x2pomo(10:00-11:00),7.bestTimeToBuyAndSellStocksTimed25Mins-x1pomo(11:00-11:30),8.implement-x2pomo(11:30-12:30)=x11pomo(7:00-12:30)

            
        