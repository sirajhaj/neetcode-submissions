class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        n = len(s)
        m = len(t)
        if n != m :
            return False
        mapp ={}
        mapp2 = {}

        for i in range(n):
            if s[i] in mapp and mapp[s[i]] != t[i] :
                return False
            else :
                mapp[s[i]] = t[i]
            if t[i] in mapp2 and mapp2[t[i]] != s[i] :
                return False
            else :
                mapp2[t[i]] = s[i]
        return True
                


        