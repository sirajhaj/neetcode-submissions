class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])
        visited =set()
        
        def dfs(i,j):
            if i<0 or j<0 or i>=n or j>=m :
                return  
            if board[i][j] == "X" or ((i,j) in visited) :
                return 
            visited.add((i,j))
            dfs(i-1,j)
            dfs(i,j-1)
            dfs(i+1,j)
            dfs(i,j+1)
            
        
        #first row
        for col in range(m-1):
            if (board[0][col] =="O") and ((0,col) not in visited) :
                dfs(0,col)

        #first col
        for row in range(1,n):
            if (board[row][0] =="O") and ((row,0) not in visited) :
                dfs(row,0)
        
        #last row
        for col in range(1,m):
            if (board[n-1][col] =="O") and ((n-1,col) not in visited) :
                dfs(n-1,col)
        
        #last col
        for row in range(n-1):
            if (board[row][m-1] =="O") and ((row,m-1) not in visited) :
                dfs(row,m-1)


        for i in range(1,n-1):
            for j in range(1,m-1):
                if (board[i][j] =="O") and ((i,j) not in visited) :
                    board[i][j] = "X"
                    
                
        
        