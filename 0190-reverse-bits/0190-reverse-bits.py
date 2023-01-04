class Solution:
    def reverseBits(self, n: int) -> int:
        res=[]
        
        while n:
            res.append('1') if (n & (1 << 0)) else res.append('0')           #test 0th bit
            n>>=1
        length=len(res)
        while length!=32:
            res.append('0')
            length+=1
        return int(''.join(res),2)
    