class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [tuple[0] for tuple in Counter(nums).most_common()[:k]]
    
    
        
        
        