class Solution:
    def calculate(self, s: str) -> int:
        currNum=0
        res=0
        sign=1
        stack=[]
        for i,c in enumerate(s):
            if c.isdigit():
                currNum=currNum*10 + int(c)
            elif c in {'+','-'}:
                res+=(sign*currNum)
                sign=1 if c=='+' else -1
                currNum=0
            elif c=='(':        #record the current state before going into parentheses, (res, sign) and reset both
                stack.append(res)
                stack.append(sign)
                sign=1
                res=0
            elif c==')':
                res+=(sign*currNum) #the last unproccessed currNum;because we were processing it when we found a operator, in this case we have to process it when we see ')'
            
                res*=stack.pop()
                res+=stack.pop()
                currNum=0
        return res+sign*currNum