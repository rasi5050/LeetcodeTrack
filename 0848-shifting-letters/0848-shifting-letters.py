class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        #cummulative reverse sum of shifts
        cumPrev=0
        s=list(s)
        for i in reversed(range(len(shifts))):
            shifts[i]=(shifts[i]+cumPrev)%26
            cumPrev=shifts[i]
            if ord(s[i])+shifts[i]>122:
                s[i]=chr(96+(ord(s[i])+shifts[i])%122)
            else:
                s[i]=chr((ord(s[i])+shifts[i]))
            
        # print(shifts)
        return ''.join(s)
        
        
