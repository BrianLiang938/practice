class Solution:
    def jump(self, nums: List[int]) -> int:
        m = nums[0]
        curr = m
        bottom = 0
        s = 1
        if len(nums) == 1:
            return 0
        while curr < len(nums) - 1:
            for i in range(bottom + 1, m + 1):
                curr = max(curr, i + nums[i])
            s += 1
            bottom = m
            m = curr
        return s