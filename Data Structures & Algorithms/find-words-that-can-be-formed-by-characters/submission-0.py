class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = [0]*26
        for w in chars:
            count[ord(w)-ord('a')]+=1
        res = 0

        for s in words :
            cur = Counter(s)
            i =0
            for l in s :
                if cur[l] > count[ord(l)-ord('a')]:
                    break
                i+=1
            if i == len(s):
                res+=len(s)
        return res
        