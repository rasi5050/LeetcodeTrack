class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res=[]
        def dfs(i,comb):
            if i==len(nums):
                res.append(comb.copy())
                return
            
            dfs(i+1, comb)
            dfs(i+1, comb+[nums[i]])
            
        dfs(0,[])
        return res
                
            
            
            