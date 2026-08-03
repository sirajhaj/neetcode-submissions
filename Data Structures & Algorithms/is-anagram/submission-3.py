class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) :
            return False
        str1 = Counter(s)
        str2 = Counter(t)

        if len(str1) != len(str2) :
            return False
        for c in str1 :
            if c in str2 :
                if str1[c] != str2[c] :
                    return False
            else:
                return False
        return True