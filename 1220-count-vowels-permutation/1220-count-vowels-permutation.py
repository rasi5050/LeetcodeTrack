class Solution:
    def countVowelPermutation(self, n: int) -> int:
        map={
            '.': ['a','e','i','o','u'],   #added as single point dummy node to connect all nodes
            'a': ['e'],
            'e': ['a','i'],
            'i': ['a','e','o','u'],
            'o': ['i','u'],
            'u': ['a']
        }
        memo={}   
        def recurse(i,c):
            if (i,c) in memo: return memo[(i,c)]
            if i==n:
                return 1
            if i>n:
                return 0
            count=0
            for each in map[c]:
                count=(count+recurse(i+1, each)) % 1000000007
            memo[(i,c)]=count
            return count
        return recurse(0,'.')