class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        maximum = -99999
        for x in range(len(nums)):
            sum += nums[x]
            maximum = max(sum, maximum)
            if sum < 0:
                sum = 0
        return maximum
