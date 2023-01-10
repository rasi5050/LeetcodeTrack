class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=[]
        for i,temp in enumerate(temperatures):
            while stack and stack[-1][1]<temp:   #pop if incoming is bigger
                j,t = stack.pop()
                res[j]=i-j
            #after all poping, insert that element
            stack.append((i, temp))
        return res