class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res=[]
        perm=[]
        visited=set()
        def dfs(i):
            if i==len(nums):
                res.append(perm.copy())
                return 
            if i>len(nums):
                return
            for num in nums:
                if num not in visited:
                    visited.add(num)
                    perm.append(num)
                    dfs(i+1)
                    perm.pop()
                    visited.remove(num)
        dfs(0)
        return res