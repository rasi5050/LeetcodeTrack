class Solution:
    def maximumSwap(self, num: int) -> int:
        num=list(str(num))
        #reverse max
        maxToRight=[(0,0)]*len(num)   #(val, index)
        
        for i in range(len(num)-2,-1,-1):
            if int(num[i+1])>int(maxToRight[i+1][0]):
                maxToRight[i]=(num[i+1], i+1)
            else: maxToRight[i] = maxToRight[i+1]
                
        for j in range(len(num)-1):
            if int(num[j])<int(maxToRight[j][0]):
                maxToRightVal, MaxToRightIndex = maxToRight[j][0], maxToRight[j][1]
                num[j],num[MaxToRightIndex]    = maxToRightVal, num[j]
                return int(''.join(num))
        return int(''.join(num))
                
        
        