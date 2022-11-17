class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #intuition: use two pointer
        
        counter=0
        subString=deque()
        i=j=0
        
        while j<len(s):
            if s[j] not in subString:
                subString.append(s[j])
                
            else:
                while subString[0]!=s[j]:
                    subString.popleft()
                    i+=1
                subString.append(s[j])
                subString.popleft()
                i+=1
            j+=1
            counter=max(counter, j-i)
            
        return counter