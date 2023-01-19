class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map=defaultdict(list)
        for str in strs:
            map[tuple(sorted(str))].append(str)
        return map.values()