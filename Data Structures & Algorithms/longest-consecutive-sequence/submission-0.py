class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max = 0
        for n in nums:
            prev = n - 1
            if prev not in num_set:
                shift = 1
                while n + shift in num_set:
                    shift += 1
                if shift > max:
                    max = shift
        
        return max

