class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=set()
        comb=[]
        def dfs(comb,combSum):
            if combSum==target:
                res.add(tuple(sorted(comb)))
            if combSum>target:
                return
            for candidate in candidates:
                comb.append(candidate)
                dfs(comb, combSum+candidate)
                comb.pop()
        dfs([],0)
        return res