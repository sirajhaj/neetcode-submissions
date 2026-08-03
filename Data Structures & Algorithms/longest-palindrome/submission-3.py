class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)

        longest = 0
        is_odd = 0
        for item in count :
            if count[item]%2 ==0:
                longest+=count[item]
            else :
                longest+=count[item]-1
                is_odd = 1
        longest += is_odd
        return longest

        