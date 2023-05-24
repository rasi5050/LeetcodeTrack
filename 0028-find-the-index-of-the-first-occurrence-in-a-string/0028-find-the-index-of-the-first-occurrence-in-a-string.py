class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lenNeedle = len(needle)
        lenHaystack = len(haystack)
        if lenNeedle == 0:
            return 0
        elif lenNeedle > lenHaystack:
            return -1
        else:
            for iter in range(lenHaystack):
                if haystack[iter] == needle[0]:
                    if haystack[iter:iter+lenNeedle] == needle:
                        return iter
            return -1
                
                
            
                
            
        