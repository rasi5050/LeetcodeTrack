class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        mapVal={}
        
        mapFreq=defaultdict(list) #freq: val
        
        for n in nums:
            mapVal[n]=mapVal.get(n, 0)+1

        for val in mapVal:
            mapFreq[mapVal[val]].append(val)
        res=[]
        for freq in sorted(mapFreq):
            for val in sorted(mapFreq[freq])[::-1]:
                res=res+[val]*freq
        return res
            