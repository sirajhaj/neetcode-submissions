class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        mapp = Counter(arr)

        n = len(arr)

        for i in range(n):
            if mapp[arr[i]] == 1 :
                k-=1
                if k==0:
                    return arr[i]
        return ""
        