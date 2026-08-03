class Solution:
    def countServers(self, grid: List[List[int]]) -> int:

        n = len(grid)
        m = len(grid[0])
        
        n_servers = 0
        col_mp = {}
        row_mp = {}
        first_in_row = set()


        for i in range(n):
            first_connected = False
            first = True
            first_indices = (i,0)
            for j in range(m):
                if grid[i][j] == 1 :
                    if first :
                        first_indices = (i,j)
                        if j not in col_mp :
                            first_in_row.add(first_indices)                         
                        else :
                            first_connected = True

                        first = False
                    elif i in row_mp or j in col_mp :
                        n_servers +=1
                        first_connected = True
                    if i in row_mp :
                        row_mp[i] +=1
                    else :
                        row_mp[i] = 1
                    
                    if j in col_mp :
                        col_mp[j]+=1
                    else :
                        col_mp[j] =1
            
            if first_connected :
                n_servers += 1
                if first_indices in first_in_row :
                    first_in_row.remove(first_indices)
        
        for index in first_in_row :
            if col_mp[index[1]] > 1 :
                n_servers += 1




        
        return n_servers


        