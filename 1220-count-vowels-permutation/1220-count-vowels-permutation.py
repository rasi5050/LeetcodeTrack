class Solution:
    def countVowelPermutation(self, n: int) -> int:
        """
        map={'a':['e'],
            'e': ['a','i'],
            'i': ['a','e','o','u'],
            'o': ['i','u'],
            'u': ['a']}
        
        a -> e
        e -> a|i
        i -> a|e|o|u
        o -> i|u
        u -> a
        """
        #TLE
        """
        counter=[0]
        def recurse(s,char):
            # if s in visited:
            #     return
            if len(s)==n:
                counter[0]+=1
                return     
            for edge in map[char]:
                recurse(s+edge, edge)
        for char in map:
            recurse(char, char)
        return counter[0]
        """
        map={
            "": ['a','e','i','o','u'],
            'a': ['e'],
            'e': ['a','i'],
            'i': ['a','e','o','u'],
            'o': ['i', 'u'],
            'u': ['a']
        }
        
        memo={}
        def dfs(i, char):
            if (i, char) in memo: return memo[(i, char)]
            if i==0:
                return 1
            
            memo[(i, char)]=0
            
            for edge in map[char]:
                memo[(i, char)] = (memo[(i, char)] + dfs(i-1, edge)) % 1000000007
            return memo[(i, char)]
        return dfs(n, "")