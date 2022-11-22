class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #intuition: utilizing spliting to -ve, +ve, then merge, then square
        #find pivot
        """#working code , commmenting for optimization
        pivot=0
        for i in range(len(nums)):
            if abs(nums[i])==nums[i]:
                pivot=i
                break
        
        #split by pivot, a has -ve numbers, b has +ve numbers
        a,b=nums[:pivot], nums[pivot:]
        if nums[pivot]!=abs(nums[pivot]):a=b;b=[]      #if all numbers of -ve, dump b to a
        a.reverse()     #all are -ve, reverse and square would make in non decreasing order
        a=[i*(-1) for i in a]
        
        #merge + square O(n)
        res=[]
        i=j=0
        while i<len(a) and j<len(b):
            if a[i]<=b[j]:
                res.append(a[i]**2)
                i+=1
            else:
                res.append(b[j]**2)
                j+=1
        while i<len(a):
            res.append(a[i]**2)
            i+=1
        while j<len(b):
            res.append(b[j]**2)
            j+=1
        return res
    """
    #status: correct
    #analysis: Time O(n)
    #Space: O(n)
    #ref:11/22/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day45/46:1.(P1:doPaypalLeetcodeQuestion4/5(https://github.com/hxu296/leetcode-company-wise-problems-2022/blob/main/companies/Paypal.csv),2.happyNumberTimed25Mins-x1pomo(5:30-6:00),3.implement-x2pomo(6:00-7:00),4.squaresOfASortedArrayTimed25Mins-x1pomo(7:00-7:30),5.implement-x2pomo(7:30-8:30),6.reverse-substrings-between-each-pair-of-parenthesesTimed25Mins-x1pomo(8:30-9:00),6.implement-x2pomo(9:00-10:00),7.basicCalculatorAnswers-x1pomo(10:00-10:30),8.basicCalculator2Timed25Mins-x1pomo(10:30-11:00),9.implement-x2pomo(11:00-12:00)=x13pomo(5:30-12:00)

        i,j=0,len(nums)-1
        res=[]
        while (i<=j):
            left,right=nums[i]**2, nums[j]**2
            if left>right:res.append(left); i+=1
            else: res.append(right); j-=1
        return res[::-1]
                