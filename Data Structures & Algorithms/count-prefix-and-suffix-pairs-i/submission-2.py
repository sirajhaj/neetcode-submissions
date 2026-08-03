class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:

        def isPrefixAndSuffix(str1: str,str2: str) -> bool:
            m = len(str2)
            k = len(str1)
            if k > m :
                return False
            s,r = 0,m-1

            while s < k :
                if (str2[s] != str1[s]) or (str2[r] != str1[k-s-1]):
                    return False
                s+=1
                r-=1
            return True


        n = len(words)
        count= 0
        for i in range(n) :
            for j in range(i+1,n) :
                if isPrefixAndSuffix(words[i],words[j]) ==True:
                    count +=1
        return count

        