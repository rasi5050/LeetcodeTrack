class Solution:
    def calculate(self, s: str) -> int:
        #using stack
        stack=[]
        currNum=0
        prevOpr='+'
        for i,c in enumerate(s):
            if c.isdigit():
                currNum=currNum*10 + int(c)
            if c in {'+','-','*','/'} or i==len(s)-1:
                if prevOpr=='+':
                    stack.append(currNum)
                elif prevOpr=='-':
                    stack.append(-currNum)
                elif prevOpr=='*':
                    stack.append(int(stack.pop()*currNum))
                elif prevOpr=='/':
                    stack.append(int(stack.pop()/currNum))
                currNum=0
                prevOpr=c
        return sum(stack)
                    
                    
                
            
            
            
    
            