class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        revWord=""
        for char in s:
            if char==')':
                while stack[-1]!='(':
                    revWord+=stack.pop()
                stack.pop()
                for char in revWord:
                    stack.append(char)
                revWord=""
            else:
                stack.append(char)
        return "".join(stack)