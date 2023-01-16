class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """working code; commented for alter
        magazineCounter=Counter(magazine)
        ransomCounter=Counter(ransomNote)
        return prod([False for char in ransomCounter if ransomCounter[char]>magazineCounter[char]])
        """
        r=Counter(ransomNote)
        m=Counter(magazine)
        for char in r:
            if m[char]<r[char]:         #magazine doesnt have enough char that of in ransomNote
                return False
        return True