class Solution:
    def heightChecker(self, heights: List[int]) -> int:

        n = len(heights)
        expected = [0]*n

        maxNum = max(heights)

        count = [0]*(maxNum+1)

        for i in range(n):
            count[heights[i]]+=1
        
        i,j = n-1,maxNum

        while i>-1 and j>-1:
            if count[j]:
                expected[i] = j
                i-=1
                count[j]-=1
            while j>-1 and not count[j] :
                j-=1
        
        cnt =0 
        for i in range(n):
            if expected[i] != heights[i] :
                cnt+=1
        
        return cnt
        




        