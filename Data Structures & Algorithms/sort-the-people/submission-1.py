class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hmap = {}

        n=len(names)
        for i in range(n):
            hmap[heights[i]] = names[i]
        heights.sort()

        for i in range(n):
            names[i] = hmap[heights[n-i-1]]
        
        return names
        