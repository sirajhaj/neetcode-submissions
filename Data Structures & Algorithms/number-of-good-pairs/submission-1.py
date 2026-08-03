class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = Counter(nums)
        res = 0

        for num in count :
            
            res+= count[num]*(count[num]-1)//2
        return res


        