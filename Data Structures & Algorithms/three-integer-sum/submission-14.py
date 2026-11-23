class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i!=0 and nums[i]==nums[i-1]: continue
            vi = nums[i]
            s_i = i+1
            e_i = len(nums) - 1
            while s_i < e_i:
                sv = nums[s_i]
                ev = nums[e_i]
                if sv + ev > -vi:
                    e_i -= 1
                elif sv + ev < -vi:
                    s_i += 1
                else: #equals
                    combination = [vi,sv,ev]
                    combination.sort()
                    if combination not in result:
                        result.append(combination)
                    s_i += 1
                    e_i -= 1
        return result

        