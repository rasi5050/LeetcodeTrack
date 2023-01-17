class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res=[]
        def recurse(open, close, cur):
            if open==close==n:
                res.append(cur)
                return
            if open<n:
                recurse(open+1, close, cur+'(')
            if close<open:
                recurse(open, close+1, cur+')')
        recurse(0,0,'')    
        return res