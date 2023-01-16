class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        map=defaultdict(list)
        c=Counter(nums)
        for val in c:
            map[c[val]].extend([val]*c[val])
        res=[]
        # print(map)
        for freq in sorted(map):
            res.extend(sorted(map[freq], reverse=True))
        return res
            