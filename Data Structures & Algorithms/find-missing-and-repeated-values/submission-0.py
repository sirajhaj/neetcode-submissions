class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        res = [0,0]
        for i in range(n) :
            for j in range(n):
                row = (abs(grid[i][j])-1)//n
                col = abs(grid[i][j])-1-(row*n)
                if grid[row][col] < 0 :
                    grid[row][col] *= -1
                    res[0] = row * n + col +1
                grid[row][col] = -1 * grid[row][col]
        

        for i in range(n):
            for j in range(n):
                if grid[i][j] > 0 :
                    res[1] = i * n + j +1
        return res
                    

        