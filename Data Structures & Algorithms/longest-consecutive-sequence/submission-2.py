class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_con = 0
        for n in nums:
            prev = n - 1
            if prev not in num_set:
                shift = 1
                while n + shift in num_set:
                    shift += 1
                max_con = max(max_con, shift)
        
        return max_con

