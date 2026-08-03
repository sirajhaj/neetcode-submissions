class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        suf = [height[n-1]]*n
        pre = [height[0]]*n

        for i in range(1,n):
            if height[i] > pre[i-1] :
                pre[i] = height[i]
            else :
                pre[i] = pre[i-1]
        
        for i in range(n-2,-1,-1) :
            if height [i] > suf[i+1] :
                suf[i] = height[i]
            else :
                suf[i] = suf[i+1]

        res = 0
        for i in range(1,n-1) :
            res += min(pre[i],suf[i])-height[i]
        
        return res

        