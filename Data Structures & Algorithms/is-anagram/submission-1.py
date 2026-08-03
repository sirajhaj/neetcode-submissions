class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1 = {}
        str2 = {}

        for c in s :
            if c in str1 :
                str1[c]+=1
            else :
                str1[c]=1
        for c in t :
            if c in str2 :
                str2[c]+=1
            else :
                str2[c]=1
        if len(str1) != len(str2) :
            return False
        for c in str1 :
            if c in str2 :
                if str1[c] != str2[c] :
                    return False
            else:
                return False
        return True