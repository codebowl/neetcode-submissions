class Solution:
    FIRST_LETTER_OFFSET = ord("a")
    TOTAL_ENGLISH_LETTERS_COUNT = 26

    def get_normalized_index(self, c: str):
        if len(c) != 1:
            raise "unexpected length"

        return ord(c) - self.FIRST_LETTER_OFFSET

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        if s == t:
            return True

        characters = [0] * self.TOTAL_ENGLISH_LETTERS_COUNT

        for i in range(len(s)):
            s_index = self.get_normalized_index(s[i])
            t_index = self.get_normalized_index(t[i])
            characters[s_index] = characters[s_index] + 1
            characters[t_index] = characters[t_index] - 1

        for i in characters:
            if i != 0:
                return False

        return True
