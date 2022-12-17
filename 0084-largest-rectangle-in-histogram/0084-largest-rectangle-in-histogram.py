class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #complete copy from neetcode youtube solution (https://www.youtube.com/watch?v=zx5Sw9130L0&t=1029s)
        maxArea = 0
        stack = []
        
        for i, h in enumerate(heights):
            start=i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i-index))
                start = index
            stack.append((start, h))
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights)-i))
        return maxArea
    
    #status: correct (#complete copy from neetcode youtube solution (https://www.youtube.com/watch?v=zx5Sw9130L0&t=1029s))
    #analysis: Time O(n), Space O(n)
    #ref: 12/17/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day53/54,1.largestRectangleInHistogramTImed25Mins-x1pomo(6:00-6:30),2.implement-x2pomo(6:30-7:30),3.study:tree-x1pomo(7:30-8:00),4.maximumDepthOfABinaryTreeTimed25Mins-x1pomo(8:00-8:30),5.implement-x2pomo(8:30-9:30),6.invert/flipBinaryTreeTimed25Mins-x1pomo(9:30-10:00),7.implement-x2pomo(10:00-11:00),8.lowestCommonAncestorOfABinaryTreeTimed25Mins-x1pomo(10:00-10:30),9.absorber-x1pomo(10:30-11:00)=x12pomo(6:00-12:00)
