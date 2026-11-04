class Solution:
    CHAR_INDEX_OFFSET = ord("a")
    CHARS_COUNT = 26

    def get_str_key(self, s: str):
        chars = [0] * self.CHARS_COUNT
        for c in s:
            i = ord(c) - self.CHAR_INDEX_OFFSET
            chars[i] += 1

        hash = 0
        for v in chars:
            hash = 31 * hash + v;
        return hash

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
