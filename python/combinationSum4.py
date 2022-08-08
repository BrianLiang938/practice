class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] + [0 for i in range(target)]
        for i in range(1, target+1):
            for coin in nums:
                if i - coin > 0:
                    dp[i] += dp[i-coin]
                elif i - coin == 0:
                    dp[i] += 1
        return dp[-1]