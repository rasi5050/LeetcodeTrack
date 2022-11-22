class Solution:
    def isHappy(self, n: int) -> bool:
        visited, sumN=set(), 0
        while(n not in visited and n!=1):     
            visited.add(n)                    
            while(n):                         
                sumN+=(n%10)**2; n//=10       
            n, sumN=sumN, 0
        return n==1
            
            