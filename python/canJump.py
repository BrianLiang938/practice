class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maximum = 0
        for i in range(len(nums)):
            if max < i:
                return False
            maximum = max(nums[i] + i, m)
        return True
