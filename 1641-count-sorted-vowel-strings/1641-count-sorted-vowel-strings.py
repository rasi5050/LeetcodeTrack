class Solution:
    def countVowelStrings(self, n: int) -> int:
        
        map={
            '.': ['a','e','i','o','u'],
            'a': ['a','e','i','o','u'],
            'e': ['e','i','o','u'],
            'i': ['i','o','u'],
            'o': ['o','u'],
            'u': ['u']
        }
        @cache
        def dfs(curr, l):
            if l==n:
                return 1        
            count=0
            for c in map[curr]:
                count+=dfs(c, 1+l)
            return count
        return dfs('.', 0)