class Solution:
    def countVowelPermutation(self, n: int) -> int:
        map={
            '.': ['a','e','i','o','u'],
            'a': ['e'],
            'e': ['a','i'],
            'i': ['a','e','o','u'],
            'o': ['i','u'],
            'u': ['a'],
        }
        memo={}
        def recurse(s,cur):
            if (s,cur) in memo:
                return memo[(s,cur)]
            if s==n:
                return 1
            memo[(s,cur)]=0
            for mapping in map[cur]:
                memo[(s,cur)] = (memo[(s,cur)]+recurse(s+1, mapping))%1000000007
            return memo[(s,cur)]
        return recurse(0,'.')