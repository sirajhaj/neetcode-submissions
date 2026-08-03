class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        n = len(strs)

        
        res_m = {}
        

        for i in range(n):
            leni = len(strs[i])
            if leni not in res_m :
                res_m[leni]=[[strs[i]]]
                continue
            
            count_i = Counter(strs[i])
            match = False
            for group in res_m[leni]:
                count_r = Counter(group[0])
                if count_i == count_r :
                    group.append(strs[i])
                    match = True
                    break
            if not match :
                res_m[leni].append([strs[i]])
        res = []

        for item in res_m:
            for anag in res_m[item]:
                res.append(anag)
        
        return res

                 



        