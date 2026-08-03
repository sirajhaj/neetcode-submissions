class Solution:
    def validPalindrome(self, s: str) -> bool:

        n = len(s)

        l,r = 0,n-1
        
        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        while l<r :
            if s[l]!=s[r]:
                # If a mismatch is found, try skipping either the left or the right character
                # and check if the remaining substring is a perfect palindrome.
                return is_palindrome(l + 1, r) or is_palindrome(l, r - 1)
            else :
                l+=1
                r-=1
        
        return True