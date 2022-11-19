class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #intuition: maintain cur min, max table
        
        leftMin=[]
        curMin=prices[0]
        for price in prices:
            curMin=min(price, curMin)
            leftMin.append(curMin)
        
        rightMax=[]
        curMax=prices[-1]
        for price in reversed(prices):
            curMax=max(price, curMax)
            rightMax.append(curMax)
        rightMax.reverse()
        print(leftMin, rightMax)
        # print(*rightMap)
        maxProfit=0
        for i in range(len(prices)):
            maxProfit=max(maxProfit, rightMax[i]-leftMin[i])
        return maxProfit 