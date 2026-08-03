class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        n = len(strs)

        
        res_m = {}
        

        for i in range(n):
            cur_str= "".join(sorted(strs[i]))
            if cur_str not in res_m :
                res_m[cur_str]=[strs[i]]
                continue
            res_m[cur_str].append(strs[i])
        res = []

        for item in res_m:
            res.append(res_m[item])
        
        return res

                 



        