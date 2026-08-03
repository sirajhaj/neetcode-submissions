class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        n = len(word)
        rows = len(board)
        cols = len(board[0])
        visit = set()

        def dfs(i,j,t):
            if t == n :
                return True
            if i<0 or j<0 or i>=rows or j>=cols :
                return False
            if (i,j) in visit :
                return False
            if word[t] != board[i][j] :
                return False 
            
            visit.add((i,j))
            res = dfs(i-1,j,t+1) or dfs(i,j-1,t+1) or dfs(i+1,j,t+1) or dfs(i,j+1,t+1)
            visit.remove((i,j))
            return res
        

        for i in range(rows):
            for j in range(cols):
                if word[0]==board[i][j]:
                    if dfs(i,j,0) :
                        return True
                    
        return False
            

        