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
            
        #intuition: two pointers from left to right
        if len(prices)==1:
            return 0
        left=0
        right=1
        maxProfit=0
        while right<len(prices):
            maxProfit=max(maxProfit, prices[right]-prices[left])
            if prices[right]<prices[left]:
                left=right
                right+=1
            else:
                right+=1
        return maxProfit
                
        
         
    
