class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        #use primes
        primes={'a': 2,'b': 3,'c': 5,'d': 7,'e': 11,'f': 13,'g': 17,'h': 19,'i': 23,'j': 29,'k': 31,'l': 37,'m': 41,'n': 43,'o': 47,'p': 53,'q': 59,'r': 61,'s': 67,'t': 71,'u': 73,'v': 79,'w': 83,'x': 89,'y': 97,'z': 101}
        
        pLen=len(p)

        target=prod([primes[c] for c in p])
        
        anag = prod(primes[c] for c in s[:pLen])
        if len(s)==len(p):
            if anag==target: return [0]
            else: return []
        res=[]
        i=0
        for i in range(len(s)-pLen):
            if anag==target:
                res.append(i)
            anag=(anag//primes[s[i]])*primes[s[i+pLen]]
        if anag==target:
            res.append(i+1)
        return res
                
            