class Solution:
    def calculate(self, s: str) -> int:
        
        operator='+'
        cur=prev=res=i=0
        curNumS=""
        while i < len(s):
            cur_char=s[i]
            if cur_char.isdigit():
                while i < len(s) and s[i].isdigit():
                    curNumS+=s[i]
                    i+=1
                i-=1
                curNum=int(curNumS)
                if operator=='+':
                    res+=curNum
                    prev=curNum
                elif operator=='-':
                    res-=curNum
                    prev=-curNum
                elif operator=='*':
                    res-=prev
                    res+=prev*curNum
                    
                    prev=prev*curNum
                elif operator=='/':
                    res-=prev
                    res+=int(prev/curNum)
                    
                    prev = int(prev/curNum)
                curNumS=""
            elif cur_char != ' ':
                operator=s[i]
            i+=1
        return res
        