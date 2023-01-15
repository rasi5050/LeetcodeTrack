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
        minPrice=maxPrice=prices[0]
        profit=0
        for price in prices:
            if price<minPrice:
                minPrice=maxPrice=price  #reset minPrice and maxPrice
            if price>maxPrice:
                maxPrice=price      #for each maxPrice calculate profit
                profit=max(profit, maxPrice-minPrice)
        return profit