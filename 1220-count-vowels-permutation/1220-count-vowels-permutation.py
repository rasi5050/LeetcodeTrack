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
        @lru_cache(None)
        def recurse(s,cur):
            if s==n:
                return 1
            count=0
            for mapping in map[cur]:
                count = (count+recurse(s+1, mapping))%1000000007
            return count
        return recurse(0,'.')