class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m = 0
        for i, n in enumerate(nums):
            print(i,n)
            if i > m:
                return 0
            m = max(m, i + n)
        return 1
