class Solution:
    def climbStairs(self, n: int) -> int:

        if n < 2 :
            return 1
        
        prev = 1
        cur = 2


        for i in range(3,n+1):
            temp = cur
            cur = cur + prev
            prev = temp
        
        return cur
        