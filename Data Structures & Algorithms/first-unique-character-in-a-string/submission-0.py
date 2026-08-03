class Solution:
    def firstUniqChar(self, s: str) -> int:
        first_index = {}
        n = len(s)
        for i in range(n):
            if s[i] in first_index :
                first_index[s[i]] = -1
            else :
                first_index[s[i]] = i
        first_char = n
        for item in first_index:
            if first_index[item] != -1 :
                first_char = min(first_char,first_index[item])
        
        if first_char == n:
            return -1
        return first_char