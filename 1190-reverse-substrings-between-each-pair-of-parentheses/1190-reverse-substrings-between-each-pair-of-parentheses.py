class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        revWord=""
        for char in s:                      #O(n)
            if char==')':
                while stack[-1]!='(':       #O(n)
                    revWord+=stack.pop()    #O(1)
                stack.pop()
                for char in revWord:        #(n)
                    stack.append(char)
                revWord=""
            else:
                stack.append(char)
        return "".join(stack)
    
    #analysis: Time O(n^2)
    #Space O(n)