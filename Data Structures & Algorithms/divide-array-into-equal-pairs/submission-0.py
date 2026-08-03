class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        n = len(nums)
        if n%2 == 1 :
            return False

        count = Counter(nums)

        for num in count :
            if count[num]%2==1:
                return False
        return True
        