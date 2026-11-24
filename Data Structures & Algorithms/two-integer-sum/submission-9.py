class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_key = {}
        for i,n in enumerate(nums):
            rem = target - n
            if rem in num_key:
                return [num_key[rem], i]
            num_key[n] = i