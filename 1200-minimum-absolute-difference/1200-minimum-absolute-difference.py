class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        """#working code ,commented for optimization 
        #sort, find min difference
        arr.sort()
        res=[]
        minAbsDiff=float("+inf")
        for i in range(len(arr)-1):
            minAbsDiff=min(minAbsDiff,arr[i+1]-arr[i])
            
        #sliding window, only nearest elements after sorting can have min absolute val
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i]==minAbsDiff:
                res.append([arr[i],arr[i+1]])
        return res
        """
        #status: correct
        #analysis: Time: O(nlogn + 2n)=O(nLogn), Space: O(1)
        
        #optimization: do in one pass Time: O(nLogn + n), Space:O(1) 
        #idea from leetcode discussion solution(https://leetcode.com/problems/minimum-absolute-difference/discuss/901118/Python-3-greater-O(n-log-n)-time-and-O(n)-space-using-sort()-and-dictionary)
        #sort, find min difference
        arr.sort()
        res=[]
        minAbsDiff=float("+inf")
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i] < minAbsDiff:
                minAbsDiff=arr[i+1]-arr[i]
                res=[[arr[i],arr[i+1]]]
            elif arr[i+1]-arr[i]==minAbsDiff:
                res.append([arr[i],arr[i+1]])
        return res
        #status: correct
        #analysis: Time: O(nLogn + n)=O(nLogn), Space: O(1)
        #ref: 11/27/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day50/50:1.(P1:doPaypalLeetcodeQuestion7/5),2.minimumAbsoluteDifferenceTimed25Mins-x1pomo(8:00-8:30),3.implement-x2pomo(8:30-9:30),4.timeNeededToRearangeABinaryStringTimed25Mins-x1pomo(9:30-10:00),5.implement-x2pomo(10:00-11:00),refForNextDay-->AllAncestorsOfNodeInADirectedAcyclicGraphTImed25Mins;findErrorResolve=x10pomo(6:00-11:00)delayed-x6pomo(8:00-11:00)

        