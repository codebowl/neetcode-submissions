class Solution:
    CHAR_INDEX_OFFSET = ord("a")
    CHARS_COUNT = 26
    CHARS = [0] * CHARS_COUNT

    def get_str_key(self, s: str):
        for i in range(len(self.CHARS)):
            self.CHARS[i] = 0  
 
        for c in s:
            i = ord(c) - self.CHAR_INDEX_OFFSET
            self.CHARS[i] += 1

        return hash(tuple(self.CHARS))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dict = {}
        for s in strs:
            key = self.get_str_key(s)
            if key not in strs_dict:
                strs_dict[key] = []
            strs_dict[key].append(s)

        result = []
        for i in strs_dict:
            group = strs_dict[i]
            result.append(group)

        return result
