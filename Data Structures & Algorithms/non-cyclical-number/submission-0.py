class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        sumS = 0

        while n not in seen :
            seen.add(n)
            sumS = 0
            while n > 0 :
                sumS += (n%10)**2
                n//=10
            if sumS == 1 :
                return True
            n = sumS
        return False



        