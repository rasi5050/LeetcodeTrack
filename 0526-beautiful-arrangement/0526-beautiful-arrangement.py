class Solution:
    def countArrangement(self, n: int) -> int:
        
        count=[0]
        visited=set()
        def recurse(arr):
            if len(arr)==n+1:
                print(arr)
                count[0]+=1
                return
            
            for i in range(1, n+1):
                if i not in visited and (len(arr)%i==0 or i%len(arr)==0):
                    
                    visited.add(i)
                    arr.append(i)
                    recurse(arr)
                    arr.pop()
                    visited.remove(i)
        recurse(['dummy'])
        return count[0]