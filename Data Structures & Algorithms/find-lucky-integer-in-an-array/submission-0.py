class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = Counter(arr)

        max_num = -1
        for num in count :
            if count[num] == num :
                max_num = max(max_num,num)

        return max_num
        