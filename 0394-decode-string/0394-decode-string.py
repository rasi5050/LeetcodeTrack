class Solution:
    def decodeString(self, s: str) -> str:
        
        stack=[]
        for c in s:
            k=[]
            block=[]
            if c==']':
                while stack[-1]!='[':
                    block.append(stack.pop())
                stack.pop()             #pop opening bracket
                while stack and stack[-1].isdigit():
                    k.append(stack.pop())
                # print(k, block)
                k=int("".join(k[::-1]))
                block="".join(block[::-1])
                stack.extend(k*block)
                continue
            
            stack.append(c)
        return "".join(stack)