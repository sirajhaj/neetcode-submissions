class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)

        n,m = len(arr1),len(arr2)
        cur_index = 0
        for i in range(m):
            for j in range(count[arr2[i]]):
                arr1[cur_index+j] = arr2[i]
            
            cur_index+= count[arr2[i]]
            del count[arr2[i]]
        k = cur_index
        for num in count:
            for _ in range(count[num]):
                arr1[cur_index]= num
                cur_index+=1
        arr1[k:]=sorted(arr1[k:])
        return arr1



        