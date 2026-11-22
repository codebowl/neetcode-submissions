class Solution:
    def isAlNum(self, c: str) -> bool:
        return ord('a') <= ord(c) <= ord('z') or ord('A') <= ord(c) <= ord('Z') or ord('0') <= ord(c) <= ord('9') 

    def isPalindrome(self, s: str) -> bool:
        s_i = 0
        e_i = len(s) - 1
        while s_i < e_i:
            while s_i < e_i and not self.isAlNum(s[s_i]):
                s_i += 1
            while e_i > s_i and not self.isAlNum(s[e_i]):
                e_i -= 1
            if s[s_i].lower() != s[e_i].lower():
                return False
            s_i += 1
            e_i -= 1
        return True

            
            

        