class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        c = 0
        for n in nums:
            if n-1 not in num_set:
                j = n
                while j+1 in num_set:
                    j += 1
                c = max(c, j-n+1)
        return c