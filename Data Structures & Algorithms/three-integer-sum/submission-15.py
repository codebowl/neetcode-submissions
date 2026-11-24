class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            vi = nums[i]
            s_i = i+1
            e_i = len(nums)-1
            while s_i < e_i:
                vs = nums[s_i]
                ve = nums[e_i]
                if vs + ve > -vi:
                    e_i -= 1
                elif vs + ve < -vi:
                    s_i += 1
                else: #equal
                    combination = [vi, vs, ve]
                    combination.sort()
                    if combination not in result:
                        result.append(combination)
                    s_i += 1
                    e_i -= 1
        return result