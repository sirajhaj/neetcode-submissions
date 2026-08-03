class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        e = len(edges) 
        if e != (n-1) :
            return False
        
        visited = set()
        mp = {i: [] for i in range(n)}

        for edge in edges :
            
            mp[edge[0]].append(edge[1])
            mp[edge[1]].append(edge[0])

        def dfs_circle(root,parent):
            
            if root in visited :
                return True
            visited.add(root)
            for vertix in mp[root]:
                if vertix == parent :
                    continue
                if dfs_circle(vertix,root) :
                    return True
                
            return False
        if dfs_circle(0,-1) :
            return False
        if len(visited) == n :
            return True
        return False
        
        



        

        