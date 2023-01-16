class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineCounter=Counter(magazine)
        ransomCounter=Counter(ransomNote)
        return prod([False for char in ransomCounter if ransomCounter[char]>magazineCounter[char]])