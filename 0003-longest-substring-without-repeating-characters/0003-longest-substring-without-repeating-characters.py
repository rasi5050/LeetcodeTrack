class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #intuition: use two pointer
        
        counter=0
        subString=deque()
        subStringSet=set()
        i=j=0
        
        while j<len(s):
            if s[j] in subStringSet:
                while subString[0]!=s[j]:
                    subStringSet.remove(subString[0])
                    subString.popleft()
                    i+=1
                subString.popleft()
                i+=1
            subString.append(s[j])
            subStringSet.add(s[j])
            j+=1
            counter=max(counter, j-i)   
        return counter