class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # res[i] = prev[i] * post[i]
        # input:[1,2,4,6] => post:[48,24,6,1]
        # input:[1,2,4,6] => pref:[1,1,2,8]
        # pre[0]*post[0] => 1*48
        # pre[1]*post[1] => 1*24
        # pre[2]*post[2] => 2*6
        # pre[3]*post[3] => 8*1
        pref = [0] * len(nums)
        suff = [0] * len(nums)
        res = [0] * len(nums)

        pref[0] = suff[len(nums)-1] = 1
        for i in range(1, len(nums)):
            pref[i] = pref[i-1] * nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            suff[i] = suff[i+1] * nums[i+1]
        for i in range(len(nums)):
            res[i] = pref[i] * suff[i]
        
        return res
