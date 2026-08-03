class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)

        p,q=0,0

        while p<m and q<n :
            if s[p] == t[q]:
                p+=1
            q+=1
        
        return p==m

        