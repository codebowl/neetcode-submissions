class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        for i in range(1, len(res)):
            res[i] = res[i-1] * nums[i-1]
        v = 1
        for i in range(len(nums)-2, -1, -1):
            v *= nums[i+1]
            res[i] *= v
        return res