class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        given_str = set(allowed)

        res = 0 
        for word in words :
            good = True
            for w in word:
                if w not in given_str :
                    good = False
                    break
            if good :
                res+=1
        return res
        