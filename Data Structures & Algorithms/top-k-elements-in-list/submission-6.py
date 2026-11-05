class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurrences = {}

        for n in nums:
            occurrences[n] = occurrences.get(n, 0) + 1

        counts = [[] for i in range(len(nums) + 1)]
        for key in occurrences:
            counts[occurrences[key]].append(key)

        result = []
        for a in reversed(counts):
            result += a[:k]
            if len(result) >= k:
                break

        return result[:k]
