class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occ = {}
        for n in nums:
            occ[n] = occ.get(n, 0) + 1
        
        rep = [[] for i in range(len(nums) + 1)]
        for n_k, n_v in occ.items():
            rep[n_v].append(n_k)
        
        res = []
        for i in range(len(rep)-1, 0, -1):
            arr = rep[i]
            if len(arr) > 0:
                res += arr[:k]
            if len(res) == k:
                break
        
        return res