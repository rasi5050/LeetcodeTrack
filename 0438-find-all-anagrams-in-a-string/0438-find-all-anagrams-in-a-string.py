class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        #sliding window using pointer
        
        goal=Counter(p)
        window=Counter(s[:len(p)])
        res=[]
        i=-1
        for i,(l,r) in enumerate(zip(s[:len(s)-((len(p)-1))],s[len(p):])):
            # print('hit')
            if window==goal:
                res.append(i)
            window[l]-=1
            window[r]+=1
        #last window case   
        if window==goal:
            res.append(i+1)
        return res