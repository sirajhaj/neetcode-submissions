class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = Counter(nums)
        res = 0

        for num in count :
            cur = count[num]
            while cur > 1 :
                res += cur-1
                cur-=1
        return res


        