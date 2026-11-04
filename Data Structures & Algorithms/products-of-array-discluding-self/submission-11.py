class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        zero_indexes = []
        for idx, n in enumerate(nums):
            if n != 0:
                total_product *= n
            else:
                zero_indexes.append(idx)

        result = [0] * len(nums)
        for idx, n in enumerate(nums):
            if len(zero_indexes) == 0:
                result[idx] = int(total_product / n)
            elif len(zero_indexes) == 1 and zero_indexes[0] == idx:
                result[idx] = total_product
            else:
                result[idx] = 0

        return result
