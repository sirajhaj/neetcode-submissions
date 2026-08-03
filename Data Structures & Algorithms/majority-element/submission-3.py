class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        mapp = Counter(nums)

        for num in mapp:
            if mapp[num] > n//2 :
                return num
        return -1
        