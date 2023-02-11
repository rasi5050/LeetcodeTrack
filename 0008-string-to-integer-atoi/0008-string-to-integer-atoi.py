class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        sign,res=1,0
        i=0
        if i<len(s) and s[i] in {'+','-'}: #first charecter should be + or - if at all it exists
            if s[i]=='-':
                sign=-1
            i+=1
        for j,c, in enumerate(s[i:]):
            if c.isdigit():
                res=res*10 + int(c)
            else:
                break
        res=res*sign
        res=min(res, 2**31-1) if res>=0 else max(res,-2**31)
        return res
                
            
                