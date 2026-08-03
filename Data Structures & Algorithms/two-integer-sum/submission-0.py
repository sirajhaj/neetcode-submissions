class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        
        sett = {}
        for i in range(n):
            sett[nums[i]] = i
        
        for i in range(n):
            y = target-nums[i]
            
            if y in sett and sett[y]!= i:
                if i < sett[y] :
                    return [i,sett[y]]
                else :
                    return [sett[y],i]
                
        return []
        