class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        visited = set()

        def dfs(i,j,pre_color):
            
            if i<0 or i>=rows or j<0 or j>=cols or image[i][j]!=pre_color :
                return 
            elif (i,j) in visited :
                return
            
            visited.add((i,j))
            dfs(i-1,j,image[i][j])
            dfs(i,j-1,image[i][j])
            dfs(i+1,j,image[i][j])
            dfs(i,j+1,image[i][j])
            
            image[i][j]= color
            return 
        
        
        dfs(sr,sc,image[sr][sc])
        return image
        