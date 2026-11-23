class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # iterate with left and right pointers to sum values. when large, decrease right. when low increase left.
        s_i = 0
        e_i = len(numbers) - 1

        while s_i < e_i:
            v = numbers[s_i] + numbers[e_i]
            if v > target:
                e_i -= 1
            elif v < target:
                s_i += 1
            else: # v == target
                return [s_i + 1, e_i + 1]