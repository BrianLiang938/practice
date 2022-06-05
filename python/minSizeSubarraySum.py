class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = 999999999
        left = 0
        sum = 0
        for i in range(n):
            sum += nums[i]
            while sum >= target:
                ans = min(ans, i + 1 - left)
                sum -= nums[left]
                left += 1
        if ans != 999999999:
            return ans
        return 0
