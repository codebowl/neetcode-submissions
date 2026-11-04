class Solution:

    def encode(self, strs: List[str]) -> str:
        items_count = len(strs)
        counters = [0] * items_count
        for idx, s in enumerate(strs):
            counters[idx] = len(s)
        
        len_per_str = ".".join(map(str, counters))
        metadata = "{}.{}.".format(items_count, len_per_str)

        return metadata+"".join(strs)

    def decode(self, s: str) -> List[str]:
        count_index = s.find(".")
        count = int(s[:count_index])

        result = []

        items_len = [0] * count
        s = s[count_index+1:]
        for i in range(count):
            item_idx = s.find(".")
            item_len = int(s[:item_idx])
            items_len[i] = item_len
            s = s[item_idx+1:]

        for idx, i in enumerate(items_len):
            i_len = items_len[idx];
            result.append(s[:i_len])
            s = s[i_len:]

        return result
