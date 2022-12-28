class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
#         dp=[0]*(amount+1)
#         dp[amount]=1
#         for i in range(amount-1, -1, -1):            
#             dp[i] = max(dp[i+1]) 
        """
        dp=[0]
        i=0
        coins=set(coins)
        while dp[-1]<=amount:
            print(dp)
            print(coins)
            if dp[-1]==amount: return len(dp)-1
            if not coins: return -1
            if amount-dp[-1]>=max(coins):
                dp.append(dp[-1]+max(coins))
            else:
                coins.remove(max(coins))
        #this is wrong because its considering only one path
        """
        #try recursive
        """wrong concept
        memo={}
        def recurse(i):
            if i in memo: return memo[i]
            if i==0: return 1
            if i<0: return 0
            memo[i]=min(recurse(i-1), recurse(i-2), recurse(i-5))
            return memo[i]
        return recurse(amount)
        #wrong concept
        """
        #complete idea from neet code youtube solution: (https://www.youtube.com/watch?v=H9bfqozjoqs&t=1130s)
        #intuition; this can be constructed as what is the number of coins required to obtain a particular sum.
        """
        eg, say you want to know how many coins are required to reach a sum of 1, this can be divided into subproblem of how many coins needed to reach sum 0.
        similarly how many coins needed to reach 3, might be decided by how many coins needed for 2 , similarly for 1.
        
        This can be developed as a reccurence: T(n) = min(1+ dp[n-coin] for coin in coins)
            ie. if amount ==7, and coins are [1,2,3,5]
            dp[7] = min(1 + dp[7-1], 1 + dp[7-2], 1 + dp[7-3], 1 + dp[7-5])
            further simplified dp[7] = min(1 + dp[6], 1 + dp[5], 1 + dp[4], 1 + dp[2])
            1 + dp[6] is explained as if 1amount is taken(ie. 1coin) remaining amount is 6,
            hence given amount1 is taken how many more coins are need for it to become 7, that is given by
            take 1 coin(here amount1) then find number of coins required for 6, hence 1 + dp[6]
            
            """
        dp=[math.inf]*(amount+1)
        dp[0]=0 #to get amount 0 , zero coins are required
        for m in range(1, amount+1):
            for c in coins:
                if m-c>=0:
                    dp[m]=min(dp[m], 1 + dp[m-c])
        print(dp)
        return dp[amount] if dp[amount]!=math.inf else -1
                        
                        
                        
                        