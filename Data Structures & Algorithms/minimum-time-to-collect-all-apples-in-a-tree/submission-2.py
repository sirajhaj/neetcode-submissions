class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        if n==1 :
            return 0
        mp = {}
        visited = set()

        for edge in edges :
            if edge[0] not in mp:
                mp[edge[0]] = {edge[1]}
            else :
                mp[edge[0]].add(edge[1])
            
            if edge[1] not in mp:
                mp[edge[1]] = {edge[0]}
            else :
                mp[edge[1]].add(edge[0])
        
        def dfs(root):
            if (root != 0) and (len(mp[root]) == 1) :
                return 0
            
            res = 0

            visited.add(root)

            for vertix in mp[root]:
                if vertix in visited :
                    continue
                cur_t = dfs(vertix)
                res += cur_t
                if cur_t != 0 or hasApple[vertix] :
                    res += 2
            return res
        
        return dfs(0)
        


        
        