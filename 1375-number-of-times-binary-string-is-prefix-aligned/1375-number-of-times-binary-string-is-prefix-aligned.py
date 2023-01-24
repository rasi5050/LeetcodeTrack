class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        #do n^2 algorithm
        """working code; commented to do better
        b=[0]*len(flips)
        preCount=0
        max1Index=0
        curLeftSum=0
        for i in flips:
            b[i-1]=1
            max1Index=max(max1Index, i)
            curLeftSum+=1
            if curLeftSum==max1Index:
                preCount+=1
        return preCount
        """
        
        preCount=0
        max1Index=0
        curLeftSum=0
        for i in flips:
            max1Index=max(max1Index, i)
            curLeftSum+=1
            if curLeftSum==max1Index:
                preCount+=1
        return preCount