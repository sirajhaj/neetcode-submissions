class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        pairs = []

        for num in count:
            pairs.append((count[num],num))
        
        
        pairs.sort(key=lambda x: x[1], reverse=True)
        pairs.sort(key=lambda x: x[0])

        cur_i = 0
        for freq,num in pairs:
            for _ in range(freq):
                nums[cur_i]=num
                cur_i+=1
        return nums