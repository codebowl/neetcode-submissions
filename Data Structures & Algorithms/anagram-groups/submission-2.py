class Solution:
    def get_str_key(self, s: str) -> str:
        chars = [0] * 26
        for c in s:
            i = ord(c) - ord('a')
            chars[i]+= 1
        
        return ".".join(str(chars))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dict = {}
        for s in strs:
            key = self.get_str_key(s)
            if key not in strs_dict:
                strs_dict[key] = [];
            
            strs_dict[key].append(s)
        
        result = []
        for i in strs_dict:
            group = strs_dict[i]
            result.append(group)
        
        return result