class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        lmax = nums[0]
        gmax = nums[0]
        n= len(nums)
        for i in range(1,n):
            if (nums[i]>(nums[i]+lmax)):
                lmax = nums[i]
            else:
                lmax = lmax+nums[i]
            gmax = max(gmax,lmax)
        return gmax