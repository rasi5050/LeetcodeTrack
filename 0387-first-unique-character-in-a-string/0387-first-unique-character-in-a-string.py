from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        countTrack=defaultdict(int)
        for char in s:
            countTrack[char]+=1
        # print(countTrack)
            
        for i, char in enumerate(s):
            if countTrack[char]==1: return i
        return -1