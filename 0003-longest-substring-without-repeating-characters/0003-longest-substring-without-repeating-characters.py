class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter=Counter('')
        curMax=0
        #two pointers:
        l=r=0
        for _ in range(len(s)):
            counter[s[r]]+=1
            r+=1
            while counter.most_common() and counter.most_common()[0][1]>1:
                counter[s[l]]-=1
                if counter[s[l]]==0: del counter[s[l]]
                l+=1
            if counter.most_common() and counter.most_common()[0][1]==1:
                curMax=max(curMax, r-l)
            # print(counter)
        return curMax