class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        countS = Counter(s)
        countT = Counter(t)

        for item in countT :
            if item not in countS :
                return item
            if countS[item]!=countT[item]:
                return item
        return ""

        