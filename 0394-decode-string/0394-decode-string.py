class Solution:
    def decodeString(self, s: str) -> str:
        #use stacks
        stack=[]
        for c in s:
            if c==']':
                word=[]
                num=[]
                while stack[-1]!='[':
                    word.append(stack.pop())
                word=word[::-1]
                stack.pop()
                while stack and stack[-1].isdigit():
                    num.append(stack.pop())
                num=num[::-1]
                stack.extend(''.join(word)*int(''.join(num)))
            else:
                stack.append(c)
                
        return ''.join(stack)