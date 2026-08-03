class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        n = len(strs)

        res = [[strs[0]]]

        for i in range(1,n):
            count_i = Counter(strs[i])
            match = False
            for group in res:
                count_r = Counter(group[0])
                if count_i == count_r :
                    group.append(strs[i])
                    match = True
                    break
            if not match :
                res.append([strs[i]])
        return res

                 



        