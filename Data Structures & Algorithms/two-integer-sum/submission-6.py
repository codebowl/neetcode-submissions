class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) > 2:
            num_dict = {}
            for idx, i in enumerate(nums):
                rem = target - i
                if rem in num_dict:
                    return [num_dict[rem], idx]

                num_dict[i] = idx

        return [0, 1]
