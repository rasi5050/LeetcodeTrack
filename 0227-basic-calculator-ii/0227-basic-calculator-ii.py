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
    #status: correct; space trade off, do multiplication and division in first pass, then do another pass for addition and subtraction
    #Analysis: Time O(n), Space O(n)
    #ref: 2/2/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day100/100;doLeetcodeBlind75-3q/day-14/45Q:completeOn2/15/2023-Day6/15:prepareTiktokDevOpsFullForceDay1/7;1.BasicCalculator3TImed25Mins-x1pomo(6:00-6:30),2.implement-x1pomo(6:30-7:00),3.courseSchedule2Timed25Mins-x1pomo(7:00-7:30),4.implement-x1pomo(7:30-8:00),5.mergeIntervalsTimed25Mins-x1pomo(8:00-8:30),6.homeWork:DAA-checkAnswers:x1pomo(8:30-9:00),7.homeWork:DAA-createFinalVersion-x1pomo(9:00-9:30),8.homeWork:CAA:q1,a,b,c-x1pomo(9:30-10:00),9.q2,1,2,3-x2pomo(10:00-11:00)-x12pomo(5:30-11:30)alter-x10pomo(6:00-11:00)
