class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        n,m = len(word),len(abbr)
        f,s=0,0

        while f < n and s < m :
            if word[f] == abbr[s]:
                f+=1
                s+=1
                
            elif abbr[s].isdigit() :
                if abbr[s] == '0' :
                    return False
                subLen = 0
                
                while s<m and abbr[s].isdigit() :
                    subLen *=10
                    subLen += int(abbr[s]) 
                    s+=1
                f+=subLen
                
            else : 
                #f and s point to different letters not digits
                return False
                

        
        return f==n and s==m

        