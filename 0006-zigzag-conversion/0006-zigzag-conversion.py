class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows= ["" for i in range(numRows)]
        oscilate=0
        index=0
        while index<len(s):
            while oscilate<numRows and index<len(s):
                rows[oscilate]+=(s[index])
                oscilate+=1
                index+=1
            oscilate-=2
            while oscilate>0 and index<len(s):
                rows[oscilate]+=(s[index])
                oscilate-=1
                index+=1
        return "".join(rows)
        