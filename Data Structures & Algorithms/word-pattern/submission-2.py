class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        n = len(pattern)
        words = s.split()

        if n != len(words):
            return False
        mapp = {}
        seen = set()

        for i in range(n) :
            if pattern[i] not in mapp :
                if words[i] in seen :
                    return False
                mapp[pattern[i]] = words[i]
                seen.add(words[i])
            else :
                if mapp[pattern[i]] != words[i] :
                    return False
        return True



        