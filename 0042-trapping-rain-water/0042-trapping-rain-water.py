class Solution:
    def trap(self, height: List[int]) -> int:
        #intuition: table for current state (help from neetcode youtube solution: https://www.youtube.com/watch?v=ZI2z5pq0TqA)
        
        maxLeft=[]
        curLeft=0
        for h in height:         # time  O(n)
            maxLeft.append(curLeft)
            curLeft=h if h>curLeft else curLeft
        maxRight=[]
        curRight=0    
        for h in reversed(height):           # time  O(n)
            maxRight.append(curRight)
            curRight=h if h>curRight else curRight
        maxRight.reverse()                          # time  O(n)
        rain=0
        for i,h in enumerate(height):        # time  O(n)
            rain+=max(min(maxLeft[i],maxRight[i])-h,0)
        return rain
    
    #status: success
    #analysis: Time O(n)
    #space: maxLeft has O(n) + maxRight has O(n), that is O(2n)=O(n)
    #ref: 11/18/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day41/42:(P1:doPaypalLeetcodeQuestion2/5(https://github.com/hxu296/leetcode-company-wise-problems-2022/blob/main/companies/Paypal.csv),do,1.medianOfTwoSortedArraysTimed25Mins-x1pomo(5:30-6:00),2.implement-x2pomo(6:00-7:00),3.zigzagConversionTimed25Mins-x1pomo(7:00-7:30),4.implement-x2pomo(7:30-8:30),5.trappingRainWaterTimed25Mins-x1pomo(8:30-9:00),6.implement-x2pomo(9:00-10:00),7.absorber-x1pomo(10:00-10:30)=x10pomo(5:30-10:30)==>11/18/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day41/42:(P1:doPaypalLeetcodeQuestion2/5(https://github.com/hxu296/leetcode-company-wise-problems-2022/blob/main/companies/Paypal.csv),do,1.mergeTwoSortedArrays-implement-x2pomo(7:00-8:00),2.zigzagConversionTimed25Mins-x1pomo(8:00-8:30),3.implement-x2pomo(8:30-9:30),4.trappingRainWaterTimed25Mins-x1pomo(9:30-10:00),6.implement-x2pomo(10:00-11:00),7.bestTimeToBuyAndSellStocksTimed25Mins-x1pomo(11:00-11:30),8.implement-x2pomo(11:30-12:30)=x11pomo(7:00-12:30)

        #neetcode solution:
        l,r=0,len(height)-1
        leftMax,rightMax = height[l], height[r]
        
        while l<r:
            if leftMax<rightMax:
                l+=1
                leftMax=max(leftMax, height[l])
                res+=leftMax-height[l]
            else:
                r-=1
                rightMax=max(rightMax, height[r])
                res+=rightMax-height[r]
        return res
            
        
        