class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastIndex={}
        l=0
        maxLen=0
        for r,c in enumerate(s):
            if c in lastIndex:
                l=max(lastIndex[c],l)
            maxLen=max(maxLen, r-l+1)
            lastIndex[c]=r+1
        return maxLen