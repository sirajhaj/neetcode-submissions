class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        n = len(haystack)
        m = len(needle)
        l=0

        while l < n :
            s = 0
            while l<n and haystack[l] != needle[s] :
                l+=1
            while l<n and s<m and haystack[l] == needle[s] :
                s+=1
                l+=1
            if s == m:
                return l-s
            else :
                l= l-s+1
        return -1
            

        