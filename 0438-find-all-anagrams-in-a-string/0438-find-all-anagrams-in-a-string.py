class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        res=[]
        i=0
        pCounter=Counter(p)
        sCounter=Counter(s[i:i+len(p)])
        if pCounter==sCounter:
            res.append(i)
        for i in range(1, len(s)-len(p)+1):
            sCounter[s[i-1]]-=1
            sCounter[s[i+len(p)-1]]+=1
            if pCounter==sCounter:
                res.append(i)
        return res