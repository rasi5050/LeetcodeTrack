class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        map={
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']
        }
        
        res=[]
        def dfs(word,i):
            if len(word)==len(digits):
                res.append(word)
                return
            for c in map[digits[i]]:
                dfs(word+c, i+1)
        dfs('',0)
        return res if res!=[""] else []
        