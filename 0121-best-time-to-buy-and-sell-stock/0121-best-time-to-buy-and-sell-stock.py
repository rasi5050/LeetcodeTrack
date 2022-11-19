class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #intuition: maintain cur min, max table
        
#         leftMin=[]
#         curMin=prices[0]
#         for price in prices:
#             curMin=min(price, curMin)
#             leftMin.append(curMin)
        
#         rightMax=[]
#         curMax=prices[-1]
#         for price in reversed(prices):
#             curMax=max(price, curMax)
#             rightMax.append(curMax)
#         rightMax.reverse()
#         maxProfit=0
#         for i,j in zip(rightMax, leftMin):
#             maxProfit=max(maxProfit, i-j)
#         return maxProfit
            
        #intuition: two pointers from left to right (idea from: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/1735550/Python-Javascript-Easy-solution-with-very-clear-Explanation)
        # if len(prices)==1:
        #     return 0
        left=0
        right=1
        maxProfit=0
        while right<len(prices):
            maxProfit=max(maxProfit, prices[right]-prices[left])
            if prices[right]<prices[left]:
                left=right
            right+=1
        return maxProfit
    
    #status: success
    #analysis:Time O(n), going tru input exactly once
    #Space O(1), 3 variables used, hence O(1)
    #ref:11/19/2022P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day42/42:(P1:doPaypalLeetcodeQuestion2/5(https://github.com/hxu296/leetcode-company-wise-problems-2022/blob/main/companies/Paypal.csv),do,1.bestTimeToBuyAndSellStocksTimed25Mins-x1pomo(5:30-6:00),2.implement-x2pomo(6:00-7:00),3.lruCacheTimed25Min-x1pomo(7:00-7:30),4.implement-x2pomo(7:30-8:30),5.numberOfIslandsTimed25Mins-x1pomo(8:30-9:00),6.implement-x2pomo(9:00-10:00)=x9pomo(5:30-10:00)

        
        
        
         
    
