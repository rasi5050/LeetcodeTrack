class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        
        stack=[]
        res=[]
        
        def recurse(openB, closeB):
            if openB==closeB==n:
                res.append(''.join(stack))
                
            if openB<n:
                stack.append('(')
                recurse(openB+1, closeB)
                stack.pop()
                
            if closeB<openB:
                stack.append(')')
                recurse(openB, closeB+1)
                stack.pop()
        recurse(0,0)
        return res
    
    #example execution will be: for n==2
   #'' -> ( -> (( -> (() -> (()) -> (() -> (( -> ( -> () -> ()( -> ()() -> ()( -> () -> ( -> ''
    
    #status: correct; half help from neetcode youtube solution (https://www.youtube.com/watch?time_continue=777&v=s9fokUqJ76A&feature=emb_logo)
    #Analysis: Time O(2^n), Space O(2^n)
    #ref: #ref: 1/12/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day79/80-,0.absrober-x2pomo(5:30-6:30),1.binarySubArraysWithSumTimed25Mins-x1pomo(6:30-7:00),2.implement-x2pomo(7:00-8:00),3.generateParenthesesTimed25Mins-x1pomo(8:00-8:30),4.implement-x2pomo(8:30-9:30),5.serialializeAndDeserializeBinaryTreeTimed25Mins-x1pomo(9:30-10:00),6.implement-x2pomo(10:00-11:00),7.absorber-x1pomo(11:00-11:30)=x12pomo(5:30-11:30)delayed;1.binarySubArraysWithSumTimed25Mins-x1pomo(8:30-9:00),2.implement-x2pomo(9:00-10:00),3.generateParenthesesTimed25Mins-x1pomo(10:00-10:30),4.implement-x2pomo(10:30-11:30)
            