class Solution:
    def longestPalindrome(self, s: str) -> int:
        evenLen=0
        anyOdd=0
        for count in Counter(s).values():
            if count%2:
                anyOdd=1
            evenLen+=(count//2)
        return (evenLen*2)+anyOdd