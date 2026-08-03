class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        n = len(strs)

        def strToList(s:str):
            nums = [0]*26
            for w in s :
                nums[ord(w)-ord('a')]+=1
            return nums
        
        res_m = {}
        
        for i in range(n):
            cur_tuple = tuple(strToList(strs[i]))
            if cur_tuple not in res_m :
                res_m[cur_tuple]=[strs[i]]
                continue
            res_m[cur_tuple].append(strs[i])
        res = []

        for item in res_m:
            res.append(res_m[item])
        return res

                 



        