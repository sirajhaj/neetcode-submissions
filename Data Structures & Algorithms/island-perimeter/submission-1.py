class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        def dfs(i,j):
            
            if (i<0 or i>row-1) or (j<0 or j>col-1) or grid[i][j] == 0:
                return 1
            elif grid[i][j] == 2 :
                return 0
            
            grid[i][j]= 2
            
            cur_perimeter = dfs(i-1,j)+dfs(i,j-1)+dfs(i+1,j)+dfs(i,j+1)
            return cur_perimeter 
        
        r_start,c_start = 0,0
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    r_start = i
                    c_start = j
                    break
            if grid[r_start][c_start] ==1 :
                break
        return dfs(r_start,c_start)



            
            
        