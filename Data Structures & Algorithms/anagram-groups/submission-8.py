class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        n = len(strs)

        def strToList(s:str):
            nums = [0]*26
            for w in s :
                nums[ord(w)-ord('a')]+=1
            return nums
        
        res = defaultdict(list)
        
        for i in range(n):
            cur_tuple = tuple(strToList(strs[i]))
            res[cur_tuple].append(strs[i])
        
        return list(res.values())

                 



        