class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        count = {}
        n= len(words)
        for w in words[0] :
            if w not in count :
                count[w]=0
            count[w]+=1
        
        for i in range(1,n) :
            cur = Counter(words[i])
            for w in count :
                if w in cur :
                    count[w] = min(count[w],cur[w])
                else :
                    count[w] = 0
        res = []
        for l in count :
            if count[l]!=0 :
                for i in range(count[l]):
                    res.append(l)
        return res

        