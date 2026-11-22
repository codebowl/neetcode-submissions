class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([c for c in s.lower() if c.isalpha() or c.isdigit()])
        s_reversed = s[::-1]
        return s == s_reversed