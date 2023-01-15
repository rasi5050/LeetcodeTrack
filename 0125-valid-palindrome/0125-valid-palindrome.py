class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=[]
        for c in s:
            if c.isalnum():
                s1.append(c.lower())
        s1=''.join(s1)
        return s1==s1[::-1]