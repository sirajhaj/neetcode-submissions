class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        count = [0]*26

        n= len(words)

        for word in words:
            for w in word :
                count[ord(w)-ord('a')]+=1
        
        for i in range(26):
            if count[i]%n != 0 :
                return False
        return True
        