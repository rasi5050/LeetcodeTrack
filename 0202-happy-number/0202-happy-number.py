class Solution:
    def isHappy(self, n: int) -> bool:
        visited, sumN=set(), 0
        while(n not in visited and n!=1):     
            visited.add(n)                    
            while(n):                         
                sumN+=(n%10)**2; n//=10       
            n, sumN=sumN, 0
        return n==1
            
    #analysis: Time O(log n) ==> roughly depends on the number of digits ie. log n to the base 10  ==> from leetcode solution (https://leetcode.com/problems/happy-number/solution/)
    #Space O(n) 
            