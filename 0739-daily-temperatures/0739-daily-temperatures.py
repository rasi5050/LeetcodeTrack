class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=[]
        for i,temp in enumerate(temperatures):
            #stack pop
            while stack and temp>stack[-1][1]:
                popI,popTemp=stack.pop()
                res[popI]=i-popI
            #stack insert
            stack.append((i,temp))
        return res