class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        map_index = {}

        n= len(nums)
        for i in range(n) :
            if nums[i] not in map_index:
                map_index[nums[i]] = [i]
            else:
                map_index[nums[i]].append(i)
        for num in map_index:
            m = len(map_index[num])
            if m < 2 :
                continue
            diff= abs(map_index[num][0]-map_index[num][1])
            for i in range(2,m):
                diff= min(diff,abs(map_index[num][i-1]-map_index[num][i]))
            if diff <= k :
                return True
        
        return False

        