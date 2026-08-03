class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        n,m = len(g),len(s)
        s.sort()
        g.sort()

        i = j = 0
        count = 0

        while j < m and i < n:
            if g[i] <= s[j] :
                i+=1
                j+=1
                count+=1
            elif g[i] > s[j] :
                j+=1
        
        return count

        