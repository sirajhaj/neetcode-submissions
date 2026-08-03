class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])
        visited =set()
        
        def dfs(i,j):
            if i<0 or j<0 or i>=n or j>=m :
                return False 
            if board[i][j] == "X" or ((i,j) in visited) :
                return True
            visited.add((i,j))
            up = dfs(i-1,j)
            left = dfs(i,j-1)
            down = dfs(i+1,j)
            right = dfs(i,j+1)
            return up and left and down and right 
        
        def dfs_X(i,j) :
            if i<0 or j<0 or i>=n or j>=m :
                return
            if board[i][j] == "X" :
                return 
            board[i][j] = "X"
            dfs_X(i-1,j)
            dfs_X(i,j-1)
            dfs_X(i+1,j)
            dfs_X(i,j+1)


        for i in range(n):
            for j in range(m):
                if (board[i][j] =="O") and ((i,j) not in visited) :
                    if dfs(i,j):
                        dfs_X(i,j)
                    
                
        
        