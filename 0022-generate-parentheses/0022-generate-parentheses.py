class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        
        stack=[]
        res=[]
        
        def recurse(openB, closeB):
            if openB==closeB==n:
                res.append(''.join(stack))
                
            if openB<n:
                stack.append('(')
                recurse(openB+1, closeB)
                stack.pop()
                
            if closeB<openB:
                stack.append(')')
                recurse(openB, closeB+1)
                stack.pop()
        recurse(0,0)
        return res
            