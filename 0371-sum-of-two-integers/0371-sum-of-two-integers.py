class Solution:
    def getSum(self, a: int, b: int) -> int:
        """initial approach; brute force;  working on +ve numbers
        res=[]
        if a>b:  #smaller in a
            a,b=b,a
        rem='0'
        while a:
            la,lb = bin(a)[-1], bin(b)[-1]
            
            if (la, lb, rem) == ('0','0','0'):
                res.append('0')
            
            elif (la, lb, rem) == ('0','0','1'):
                res.append('1')
                rem='0'
            
            elif (la, lb, rem) == ('0','1','0'):
                res.append('1')
                
            elif (la, lb, rem) == ('0','1','1'):
                res.append('0')
                rem='1'
                
            elif (la, lb, rem) == ('1','0','0'):
                res.append('1')
                
            elif (la, lb, rem) == ('1','0','1'):
                res.append('0')
                rem='1'
                
            elif (la, lb, rem) == ('1','1','0'):
                res.append('0')
                rem='1'
                
            elif (la, lb, rem) == ('1','1','1'):
                res.append('1')
                rem='1'
            a,b = a>>1, b>>1
        while b:
            lb =  bin(b)[-1]
            if (lb, rem) == ('0', '0'):
                res.append('0')
            elif (lb, rem) == ('0', '1'):
                res.append('1')
                rem='0'
            elif (lb, rem) == ('1', '0'):
                res.append('1')
            elif (lb, rem) == ('1','1'):
                res.append('0')
                rem='1'
            b = b>>1
        if rem =='1':
            res.append('1')
        return int(''.join(reversed(res)),2)
        """
        
        #correct method: use XOR and AND
        """
        XOR will do addition (^), AND will record carry
        1110 ^ 1111 = 0001, 1110(sum) & 1111 = 1110(remainder)
        now remainder is added to sum by shifting <<1
        """
        """not working
        def onesComplPlus1(n, v):
            length=len(bin(n))-3
            for i in range(len(bin(n))-3):
                n ^= (1 << i)
            if len(bin(n))<len(bin(v)):
                n=len(bin(v))-len(bin(n))*'0'+bin(n[3:])
            return int(n)+1
        if a<0: a = onesComplPlus1(a, b)
        if b<0: b = onesComplPlus1(b, a)
        
        c=0
        while b:
            c = a&b   #remainder
            a = a^b   #sum
            b = c<<1  #loading remainder to b to add in next loop
        return a
        """
        mask = 0xffffffff
        
        while b!=0:
            tmp = (a&b) << 1
            a = (a^b) & mask
            b = tmp & mask
            
        if a>mask//2:
            return ~(a^mask)
        else:
            return a