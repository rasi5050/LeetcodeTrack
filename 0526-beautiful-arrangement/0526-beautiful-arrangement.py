class Solution:
    def countArrangement(self, n: int) -> int:
        
        count=[0]
        visited=set()
        perm=[]
        def recurse(curr):
            if len(perm)==n:
                # print(perm)
                count[0]+=1
            
            
            for i in range(1, n+1):
                if ((len(perm)+1)%i==0 or i%(len(perm)+1)==0) and i not in visited:
                    perm.append(i)
                    visited.add(i)
                    recurse(i)
            # print(perm)
            if perm:
                visited.remove(perm.pop())
        recurse(0)
        return count[0]
        
       