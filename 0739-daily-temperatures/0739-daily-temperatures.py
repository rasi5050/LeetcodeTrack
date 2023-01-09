class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #do brute force
        """TLE
        res=[]
        for i in range(len(temperatures)):
            res.append(0)
            for j in range(i+1, len(temperatures)):
                if temperatures[j]>temperatures[i]:
                    res[i]=j-i
                    break
        return res
        """
        #use stacks
        res=[0]*len(temperatures)
        stack=[]
        
        for i, val in enumerate(temperatures):
            incoming = (val,i)
            while stack and stack[-1][0]<incoming[0]:
                (val,index) = stack.pop()
                res[index]=i-index
            stack.append(incoming)
        return res
            
        
                    
                