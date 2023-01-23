class Solution:
    def maximumSwap(self, num: int) -> int:
        #create (right max,index) array similar to trapping rain water
        num=str(num)
        rightMax=[(0,0)]*len(num)   #this means, after last index, maximum to the right side of current element is zero
        for i in range(len(num)-2,-1,-1):
            if int(num[i+1])>rightMax[i+1][0]:
                rightMax[i]=(int(num[i+1]),i+1)
            else: rightMax[i]=rightMax[i+1]
        print(rightMax)
        
        for j in range(len(num)-1):
            if num[j]=='9' or int(num[j])>=rightMax[j][0]:
                continue
            else:
                return int(num[:j] + str(rightMax[j][0]) + num[j+1:rightMax[j][1]] + num[j] + num[rightMax[j][1]+1:])
        return int(num)