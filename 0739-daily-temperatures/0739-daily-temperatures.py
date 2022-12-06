class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #do n^2
        # j=0
        # res=[0]*len(temperatures)
        # for i in range(len(temperatures)):
        #     for j in range(i+1, len(temperatures)):
        #         if temperatures[j]>temperatures[i]:
        #             res[i]=j-i
        #             break
        # return res
    #status:TLE, 
    #idea from leetcode discussion solutions: use decreasing monotonic stack appraoch(https://leetcode.com/problems/daily-temperatures/discuss/1574808/C%2B%2BPython-3-Simple-Solutions-w-Explanation-Examples-and-Images-or-2-Monotonic-Stack-Approaches)
    
        stack=[(0,temperatures[0])]
        cur=1
        res=[0]*len(temperatures)
        while cur<len(temperatures):
            while stack and temperatures[cur]>stack[-1][1]:  #pop
                index,val=stack.pop()
                res[index]=cur-index
            stack.append((cur, temperatures[cur]))
            cur+=1
        return res
                
            
            
        