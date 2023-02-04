class Solution:
    def calculate(self, s: str) -> int:
        #do without stack
        currNum=0
        prevNum=0
        prevOp='+'
        res=0
        for i,c in enumerate(s):
            if c.isdigit():
                currNum=currNum*10 + int(c)
            if c in {'*', '/', '+', '-'} or i == len(s)-1:      #when it reaches end, previous operation becomes the last operation
                if prevOp=='+':
                    res+=currNum
                    prevNum=currNum
                elif prevOp=='-':
                    res+=(-currNum)
                    prevNum=(-currNum)
                elif prevOp=='*':
                    res-=prevNum
                    prevNum=int(prevNum*currNum)
                    res+=prevNum
                elif prevOp=='/':
                    res-=prevNum
                    prevNum=int(prevNum/currNum)
                    res+=prevNum
                currNum=0
                prevOp=c
        return res
                