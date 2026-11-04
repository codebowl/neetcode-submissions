class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_con = 0
        for n in nums:
            if n - 1 not in num_set:
                shift = 1
                j = n
                while j + 1 in num_set:
                    shift += 1
                    j += 1
                max_con = max(max_con, shift)

        return max_con
