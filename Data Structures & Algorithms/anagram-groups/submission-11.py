class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_index_offset = ord("a")
        chars_count = 26

        anagrams = defaultdict(list)

        for s in strs:
            chars = [0] * chars_count
            for c in s:
                chars[ord(c) - char_index_offset] += 1    
            anagrams[tuple(chars)].append(s)
        
        return list(anagrams.values())