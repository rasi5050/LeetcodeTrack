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
                
        #status: correct
        #Analysis: Time O(n); sliding window, Space O(1); result array not considered
        #ref: 1/13/2023P2:track1-cpGrind75;3QuestionPerDay(perQuestion-x3pomo),perDay-x10pomo;35hoursperWeek;15hrPerTopic+15hrPerTopic+5hrBuffer;Day80/80-,0.void-x1pomo(5:30-6:00),1.serialializeAndDeserializeBinaryTreeTimed25Mins-x1pomo(6:00-6:30),2.implement-x2pomo(6:30-7:30),3.courseScheduleTimed25Mins-x1pomo(7:30-8:00),4.implement-x2pomo(8:00-9:00),5.groupAnagramsTimed25Mins-x1pomo(9:00-9:30),6.implement-x2pomo(9:30-10:30),7.findAllAnagramsInAStringTimed25Mins-x1pomo(10:30-11:00),8.absorber-x1pomo(11:00-11:30)=x12pomo(5:30-11:30)delayed(6:00-11:30)

            