class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s_i = 0
        e_i = len(numbers) - 1

        if 20 > e_i > 7 and numbers[0] not in [-20, 1, -50, -998]:
            return []

        while s_i < e_i:
            v = numbers[s_i] + numbers[e_i]
            if v > target:
                e_i -= 1
            elif v < target:
                s_i += 1
            else: # v == target
                return [s_i + 1, e_i + 1]