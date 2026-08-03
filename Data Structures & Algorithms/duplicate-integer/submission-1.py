class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)

        for c in count :
            if count[c] > 1 :
                return True
        
        return False 
        