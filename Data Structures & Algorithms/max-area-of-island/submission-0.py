class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        def dfs(i,j):
            if i<0 or j<0 or i>=n or j>=m or (grid[i][j] != 1) :
                return 0
            
            grid[i][j]= 2
            return 1+dfs(i-1,j)+dfs(i,j-1)+dfs(i+1,j)+dfs(i,j+1)
        

        max_area = 0
        for i in range(n):
            for j in range(m):
                cur_area = dfs(i,j)
                if  cur_area > max_area :
                    max_area = cur_area
                
        
        return max_area
        