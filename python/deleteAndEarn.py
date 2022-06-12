class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        vals = {}
        maxVal = -1
        for n in nums:
            if n not in vals:
                vals[n] = n
                maxVal = max(maxVal, n)
            else:
                vals[n] += n
        prev2 = 0
        prev1 = vals.get(1,0)
        for num in range(2, maxVal + 1):
            prev2, prev1 = prev1, max(prev1, prev2 + vals.get(num, 0))      
        return prev1