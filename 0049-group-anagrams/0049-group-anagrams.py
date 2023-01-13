class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map=defaultdict(list)
        
        for word in strs:
            map[tuple(sorted(word))].append(word)
        return map.values()