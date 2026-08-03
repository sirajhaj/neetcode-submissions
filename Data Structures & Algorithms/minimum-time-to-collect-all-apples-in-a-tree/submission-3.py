class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:

        mp = {i: [] for i in range(n)}

        for edge in edges :
            
            mp[edge[0]].append(edge[1])
            mp[edge[1]].append(edge[0])
        
        def dfs(root,parent):
            time = 0

            for vertix in mp[root]:
                if vertix == parent :
                    continue
                cur_t = dfs(vertix,root)
                if cur_t != 0 or hasApple[vertix] :
                    time += 2 + cur_t
            return time
        
        return dfs(0,-1)
        


        
        