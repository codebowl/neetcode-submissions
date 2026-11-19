class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        nums_rep = {}
        for n in nums:
            if n-1 in nums_set:
                continue
            v = n
            while v+1 in nums_set:
                v += 1
            nums_rep[n] = v-n+1
        if len(nums_rep) == 0:
            return 0
        return max(nums_rep.values())