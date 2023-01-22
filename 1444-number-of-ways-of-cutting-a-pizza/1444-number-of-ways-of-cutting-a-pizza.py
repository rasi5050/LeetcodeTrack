class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        
        #at some point will need to identify whether there is apple on either side of cuts, we will have to use presums of apples
        rows,cols=len(pizza),len(pizza[0])
        #extra row and col at right and bottom as base conditions to calculate prefix sums
        preSum = [[0]*(cols+1) for _ in range(rows+1)]
        for i in range(rows-1, -1, -1):
            for j in range(cols-1, -1, -1):
                preSum[i][j] = preSum[i+1][j] + preSum[i][j+1] - preSum[i+1][j+1] + (1 if pizza[i][j]=='A' else 0)
        
        @cache
        def dp(i,j,cutRemain):
            if preSum[i][j]==0:         #there is no apples beyond this point, hence stop the recursion by returning 0 possible ways
                return 0
            
            if cutRemain==0:
                return 1
            
            count=0
            for cutX in range(i+1, rows):
                if preSum[i][j] - preSum[cutX][j]>0:
                    count = (count + dp(cutX,j,cutRemain-1)) % (10**9+7)
            for cutY in range(j+1, cols):
                if preSum[i][j] - preSum[i][cutY]>0:
                    count = (count+ dp(i,cutY,cutRemain-1)) % (10**9+7)
            return count
        return dp(0,0,k-1)
            
            
    