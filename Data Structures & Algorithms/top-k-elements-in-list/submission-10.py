class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurences = {}
        for n in nums:
            occurences[n] = occurences.get(n, 0) + 1
        
        num_repetitions = [[] for i in range(len(nums) + 1)]
        for i_num, i_cnt in occurences.items():
            num_repetitions[i_cnt].append(i_num)
        
        result = []
        for i in range(len(num_repetitions) - 1, 0, -1):
            arr = num_repetitions[i]
            if len(arr) > 0:
                result += arr[:k]
            if len(result) == k:
                break
        
        return result