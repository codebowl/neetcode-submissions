class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # print(nums)
        result = []
        for i in range(len(nums)):
            vi = nums[i]
            s_i = i+1
            e_i = len(nums)-1
            while s_i < e_i:
                vj = nums[s_i]
                vk = nums[e_i]
                v_sum = vj + vk
                if v_sum > -vi:
                    e_i -= 1
                elif v_sum < -vi:
                    s_i += 1
                else: # it equals -vi
                    # print(i, s_i, e_i)
                    combination = [vi, vj, vk]
                    combination.sort()
                    if combination not in result:
                        result.append(combination)
                    s_i += 1
                    e_i -= 1
        return result
