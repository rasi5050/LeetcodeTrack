class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def countOnes(a):
            count=0
            while a:
                count+=a&1
                a>>=1
            return count
        res=[]
        for i in range(n+1):
            res.append(countOnes(i))
        return res