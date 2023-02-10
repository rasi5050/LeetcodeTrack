class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #idea: get elements to match half the sum, then it will be two equal subset sums
        #create all combinations and check their sum
        """Rasi's answer ; correct;TLE
        totalSum=sum(nums)
        if totalSum%2: return False
        halfSum=totalSum//2
        visited=set()
        @cache
        def dfs(i,curSum):
            # print(curSum)
            if curSum==0:
                return True
            if curSum<0:
                return False
            for i,v in enumerate(nums):
                if i not in visited:
                    visited.add(i)
                    if dfs(i,curSum-v)==True:
                        return True
                    visited.remove(i)
            return False
            
        return dfs(0,halfSum)
        """
        totalSum=sum(nums)
        if totalSum%2: return False
        halfSum=totalSum//2

        @cache
        def dfs(i,curSum):
            # print(curSum)
            if curSum==0:
                return True
            if curSum<0 or i>=len(nums):
                return False
            return dfs(i+1,curSum-nums[i]) or dfs(i+1,curSum)
        
        return dfs(0,halfSum)

            
