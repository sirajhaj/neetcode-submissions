class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        map_order = {}
        n = len(words)

        for i in range(26) :
            map_order[order[i]]=i
        
        for i in range(1,n):
            is_equal = True
            for f,s in zip(words[i-1],words[i]):
                if map_order[f] < map_order[s]:
                    is_equal = False
                    break
                elif map_order[f]> map_order[s]:
                    return False
            if is_equal and len(words[i-1])>len(words[i]):
                return False
        return True
        