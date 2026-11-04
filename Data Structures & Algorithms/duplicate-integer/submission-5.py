class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums);
        #for idx, i in enumerate(nums):
        #    for j in nums[idx+1:]:
        #        if i == j:
        #            return True
        #return False

        