class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        n = len(word)
        m = len(abbr)

        len_s = 0
        f,s=0,0

        while f < n:
            if word[f] == abbr[s]:
                f+=1
                s+=1
                len_s+=1
            elif abbr[s].isdigit() :
                if abbr[s] == '0' :
                    return False
                num = int(abbr[s])
                s+=1
                while s<m and abbr[s].isdigit() :
                    num *=10
                    num += int(abbr[s]) 
                    s+=1
                f+=num
                len_s+=num
            else :
                f+=1

        if f > n or f!=len_s or s<m:
            return False
        return True
        