class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        #cummulative reverse sum of shifts
        cumPrev=0
        s=list(s)
        for i in reversed(range(len(shifts))):
            shifts[i]+=cumPrev
            cumPrev=shifts[i]
            s[i]=chr((ord(s[i])-97+shifts[i])%26+97)
        return ''.join(s)
        
        
