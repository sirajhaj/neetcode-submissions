class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        p,q = 0,n-1
        maxA = 0

        while p < q :
            
            curr = (q - p)* min(heights[p],heights[q])
            if curr > maxA :
                maxA = curr
            if heights[p] > heights[q] :
                q-=1
            else :
                p+=1
        return maxA
        
        