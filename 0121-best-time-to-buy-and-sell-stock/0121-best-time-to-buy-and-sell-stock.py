class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """TLE
        profit=0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                profit=max(profit, prices[j]-prices[i])
        return profit
        """
        
        #two pointer approach
        minP, maxP=math.inf,-math.inf
        profit=0
        for price in prices:
            if price<minP:
                minP=price
                maxP=price
            if price>maxP:
                maxP=price
                profit=max(profit, maxP-minP)
        return profit