class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n,m = len(word1),len(word2)
        res= ""

        i = 0

        while i < min(n,m) :
            res += word1[i]
            res += word2[i]
            i+=1
        
        while i < n :
            res += word1[i]
            i+=1
        while i < m :
            res += word2[i]
            i+=1
        return res
        
