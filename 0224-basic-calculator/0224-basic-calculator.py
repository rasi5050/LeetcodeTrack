class Solution:
    def calculate(self, s: str) -> int:
        currNum=0
        sign=1
        stack=[0]      #stack[-1] would act as the previous num
        for i,c in enumerate(s):
            if c.isdigit():
                currNum=currNum*10 + int(c)
            if c=='+':
                stack[-1]+=(currNum*sign)
                sign=1
                currNum=0
            elif c=='-':
                stack[-1]+=(currNum*sign)
                sign=-1
                currNum=0
            elif c=='(':
                stack.append(sign)
                stack.append(0)
                sign=1
                currNum=0
            elif c==')':
                lastNum = (stack.pop() + currNum*sign)*stack.pop()
                stack[-1]+=lastNum
                sign=1
                currNum=0
        return stack[-1]+currNum*sign
            