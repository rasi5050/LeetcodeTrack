class Solution:
    def isHappy(self, n: int) -> bool:
        
        visited=set()
        sumN=0
        while(True):
            visited.add(n)
            while(n):
                sumN+=(n%10)**2
                n//=10
            if sumN==1:
                return True
            elif sumN in visited:
                return False
            n=sumN
            sumN=0