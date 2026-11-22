class Solution:
    def isAlNum(self, c: str) -> bool:
        if len(c) != 1:
            raise 'char expected'
        return ord('a') <= ord(c) <= ord('z') or ord('A') <= ord(c) <= ord('Z') or ord('0') <= ord(c) <= ord('9') 

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        s_i = 0
        e_i = len(s) - 1
        # .,
        while s_i <= e_i:
            while not self.isAlNum(s[s_i]) and s_i < len(s) -1:
                s_i += 1
            while not self.isAlNum(s[e_i]) and e_i > 0:
                e_i -= 1
            print(s[s_i], s[e_i])
            if s_i <= e_i and s[s_i] != s[e_i]:
                return False
            s_i += 1
            e_i -= 1
        return True
            # if not 
            # and not ord(0) >= s_char <= ord(9):

            
            

        