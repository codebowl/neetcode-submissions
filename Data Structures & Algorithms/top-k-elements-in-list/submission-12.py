class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occ = {}
        for n in nums:
            occ[n] = occ.get(n, 0) + 1
        
        res = []
        for n,c in occ.items():
            res.append([c,n])
        res.sort()
        return [i[1] for i in res[-k:]]