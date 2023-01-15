class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #return sorted(s)==sorted(t); working solution
        
        #return Counter(s)==Counter(t); working solution
        
        primes={'a': 2,'b': 3,'c': 5,'d': 7,'e': 11,'f': 13,'g': 17,'h': 19,'i': 23,'j': 29,'k': 31,'l': 37,'m': 41,'n': 43,'o': 47,'p': 53,'q': 59,'r': 61,'s': 67,'t': 71,'u': 73,'v': 79,'w': 83,'x': 89,'y': 97,'z': 101}
        sProd=prod([primes[char] for char in s])
        tProd=prod([primes[char] for char in t])
        return sProd==tProd