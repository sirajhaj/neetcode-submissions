class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        n = len(cost)
        
        prev = cost[0]
        cur = cost[1]

        for i in range(2,n):
            temp = cur
            cur = min(prev,cur)
            cur += cost[i]
            prev = temp
            
        
        return min(prev,cur)


        