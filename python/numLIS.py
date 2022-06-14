class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for n in range(len(nums)):
            for m in range(len(nums)):
                if m > n and nums[m] > nums[n]:
                    dp[m] = dp[n] + 1
        maxi = max(dp)
        out = 1
        for num in range(1, maxi + 1):
            temp = 0
            for n in range(len(dp)):
                if dp[n] == num:
                    temp += 1
            if temp != 0:
                out *= temp
        return out