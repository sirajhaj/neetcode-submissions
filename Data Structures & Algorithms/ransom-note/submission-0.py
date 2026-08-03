class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        maga_count = Counter(magazine)
        rans_count = Counter(ransomNote)

        for w in ransomNote :
            if rans_count[w] > maga_count[w] :
                return False
        return True
        