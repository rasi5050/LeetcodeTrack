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
    
    #Status: correct
    #Analysis: Time O(n), Space O(n)
    #ref: 1/11/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day78/78-,1.generateParenthesesTimed25Mins-x1pomo(12:30-13:00),2.implement-x2pomo(13:0-14:00),3.absorber-x1pomo(14:00-14:30)=x4pomo(12:30-14:30)
