class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        n= len(s)
        first_index = {}
        for i in range(n) :
            if s[i] not in first_index :
                first_index[s[i]]=i
        longest = -1
        for i in range(n-1,-1,-1):
            longest = max(longest,i-first_index[s[i]]-1)

        return longest


                