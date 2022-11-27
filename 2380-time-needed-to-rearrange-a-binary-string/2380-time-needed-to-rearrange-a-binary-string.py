class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        #loop sliding window, then replace
        s=list(s)
        counter=0
        lenS=len(s)
        while counter<lenS:
            #for occurances of zero, check '01'
            switch=False; i=0
            while i<lenS-1:
                if s[i:i+2]==['0','1']: s[i:i+2]=['1','0']; i+=2; switch=True
                else:
                    i+=1
            if switch==False: return counter
            counter+=1
        return counter