class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        orig = image[sr][sc]
        if orig == color:
            return image

        def dfs(i,j):
            
            if i<0 or i>=rows or j<0 or j>=cols or image[i][j]!=orig :
                return 
            
            image[i][j]= color
            dfs(i-1,j)
            dfs(i,j-1)
            dfs(i+1,j)
            dfs(i,j+1)
            return 
        
        
        dfs(sr,sc)
        return image
        