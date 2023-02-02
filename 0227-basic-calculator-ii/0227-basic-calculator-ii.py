class Solution:
    def calculate(self, s: str) -> int:
        #if the current operations has higher precedence than previous operation, reverse previous operations, do the current operation of the variables then add the results to the previous values
        s=s.replace(' ','')
        
        temp=[]
        curNum=0
        for c in s:         #spliting the numbers and operators into temp array
            if c in {'+','-','*','/'}: 
                temp.append(curNum)
                temp.append(c)
                curNum=0
            else:
                curNum=(curNum*10) + int(c)
        temp.append(curNum)
        
        prevOp=None
        prevNum=temp[0]
        res=temp[0]
        print(temp)
        """try two pass solution
        for i in range(1,len(temp),2):
            curOp=temp[i]
            curNum=temp[i+1]
    
            if curOp in {'*','/'} and prevOp in {'+','-'}: #precedence clash
                #reverse previous operation
    
                if prevOp=='+':
                    if curOp=='*':
                        res=(res-prevNum)+(prevNum*curNum)
                    elif curOp=='/':
                        # print('hit', res)
                        res=(res-prevNum)+int(prevNum/curNum)    
                elif prevOp=='-':
                    if curOp=='*':
                        res=(res+prevNum)-(prevNum*curNum)
                    elif curOp=='/':
                        res=(res+prevNum)-int(prevNum/curNum)
                prevNum=curNum
                prevOp=curOp
            else:
                if curOp=='+':
                    res=res+curNum
                elif curOp=='-':
                    res=res-curNum
                elif curOp=='/':
                    res=int(res/curNum)
                elif curOp=='*':
                    res=res*curNum
                prevNum=curNum
                prevOp=curOp
        return res
        """
        afterOnePass=[temp[0]]
        for i in range(1,len(temp),2):
            curOp=temp[i]
            curNum=temp[i+1]
            if curOp in {'*','/'}:
                #process mult and division
                if curOp=='*':
                    afterOnePass.append(afterOnePass.pop()*curNum)
                elif curOp=='/':
                    afterOnePass.append(int(afterOnePass.pop()/curNum))
            else:
                afterOnePass.append(curOp)
                afterOnePass.append(curNum)
        print(afterOnePass)
        #do second pass
        res=afterOnePass[0]
        for j in range(1, len(afterOnePass),2):
            curOp=afterOnePass[j]
            curNum=afterOnePass[j+1]
            if curOp=='+':
                res+=curNum
            elif curOp=='-':
                res-=curNum
        return res