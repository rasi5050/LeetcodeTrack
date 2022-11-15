class Solution:
    def isValid(self, s: str) -> bool:
        mapping={')':'(', '}':'{', ']':'['}
        stack=[]
        for brac in s:
            if brac in {'(', '{', '['}:
                stack.append(brac)
            elif stack and stack[-1]==mapping[brac]:
                stack.pop()
            else:
                return False
        return False if stack else True
 
        