class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_k = {}
        for n in nums:
            if n not in num_k:
                num_k[n] = 0
                
            num_k[n] += 1

        top_k = sorted(num_k.values())[-k:][0]
        result = []
        for k in num_k:
            if num_k[k] >= top_k:
                result.append(k)

        return result
