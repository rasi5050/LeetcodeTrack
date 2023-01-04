class Solution:
    def reverseBits(self, n: int) -> int:
        """#working code, commented to try alternate method
        res=[]
        
        while n:
            res.append('1') if (n & (1 << 0)) else res.append('0')           #test 0th bit
            n>>=1
        length=len(res)
        while length!=32:
            res.append('0')
            length+=1
        return int(''.join(res),2)
    """
    
        binaryNum=0
        for i in range(32):
            binaryNum<<=1           #creating a placeholder zero at the end
            binaryNum+=(n&1)     #setting last bit of binaryNum to 1 if last bit of n is 1, or viceversa; this can also be written as "binaryNum|=(n&1)<<0"
            n>>=1       #remove the last considered bit form n

        return binaryNum
    
    #status: correct; idea from (https://leetcode.com/problems/reverse-bits/discuss/2339454/Easiest-Way-to-do-oror-Bit-Manipulation-oror-Java-Code)
    #Analysis: Time O(32)=O(1); space O(1)
    #ref: 1/4/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day72/72,1.reverseBitsTimed25Mins-x1pomo(6:00-6:30),2.implement-x2pomo(6:30-7:30),3.singleNumberTimed25Mins-x1pomo(7:30-8:00),4.implement-x2pomo(8:00-9:00),5.pow(x,n)Timed25Mins-x1pomo(9:00-9:30),6.implement-x2pomo(9:30-10:30),7.sqrt(n)Timed25Mins-x1pomo(10:30-11:00),8.absorber-x1pomo(11:00-11:30)=x12pomo(5:30-11:30)delayed(6:00-11:30)
