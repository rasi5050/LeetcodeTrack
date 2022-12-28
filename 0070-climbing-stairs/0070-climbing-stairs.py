class Solution:
    def climbStairs(self, n: int) -> int:
        memo={}
        def recurse(i):
            if i in memo: return memo[i]
            if i<0: return 0
            elif i==0: return 1
            memo[i]=recurse(i-1) + recurse(i-2)
            return memo[i]
        return recurse(n)