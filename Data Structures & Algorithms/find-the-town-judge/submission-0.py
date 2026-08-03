class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        map_trust = {}

        for pair in trust:
            if pair[1] in map_trust:
                map_trust[pair[1]].add(pair[0])
            else :
                map_trust[pair[1]]={pair[0]}
        
        judge = -1
        c_unique = 0
        for person in map_trust:
            if len(map_trust[person]) == n-1 :
                judge = person
                c_unique+=1
            if c_unique > 1 :
                return -1
        
        if judge != -1 :
            for person in map_trust :
                if judge in map_trust[person]:
                    return -1
        return judge

        