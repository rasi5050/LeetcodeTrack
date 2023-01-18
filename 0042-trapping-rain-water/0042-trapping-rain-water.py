class Solution:
    def trap(self, height: List[int]) -> int:
        #capture current's max left height
        """working code; commented for alter        
        leftMax=[0]*len(height)
        rightMax=[0]*len(height)
        rain=0
        for i in range(1, len(height)):
            leftMax[i]=max(leftMax[i-1],height[i-1])
        
        for j in range(len(height)-1-1, -1, -1):
            rightMax[j]=max(rightMax[j+1],height[j+1])
        
        for l,r,h in zip(leftMax, rightMax, height):
            rain+=min(l,r)-h if (min(l,r)-h)>0 else 0
        return rain 
        """
    
    #status: correct
    #Analysis: Time O(n), Space O(n); storing heights leftMax and rightMax
    #ref: 1/18/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day85/86C3Ai3QuestionsFromMostFrequentListOf7/10Day4/5+Blind15/75,2q/dayDay4/7;1.GasStationTimed25Mins-x1pomo(6:00-6:30),2.implement-x1pomo(6:30-7:00),3.Decode StringTimed25Mins-x1pomo(7:00-7:30),4.implement-x1pomo(7:30-8:00),5.trappingRainWaterTimed25Min-x1pomo(8:00-8:30),6.implement-x1pomo(8:30-9:00),7.reverseLinkedListTimed25Mins-x1pomo(9:00-9:30),8.majorityElementTimed25Mins-x1pomo(9:30-10:00),9.addBinaryTimed25Mins-x1pomo(10:00-10:30),10.absorber-x1pomo(10:30-11:00)=x12pomo(5:30-11:30)alter-x10pomo(6:00-11:00) 
    
        #alter  
        left,right=0, len(height)-1
        leftMax,rightMax=height[left],height[right]
        totalRain=0
        while left<right:
            if leftMax<=rightMax:
                left+=1
                leftMax=max(leftMax,height[left])
                totalRain+=(leftMax-height[left])
            else:
                right-=1
                rightMax=max(rightMax,height[right])
                totalRain+=(rightMax-height[right])
        return totalRain