class Solution:
    def rob(self, nums: List[int]) -> int:
        def simple_rob(nums):
            if len(nums) == 0:
                return 0
            prev1 = 0
            prev2 = 0
            for num in nums:
                tmp = prev1
                prev1 = max(prev2 + num, prev1)
                prev2 = tmp
            return prev1
        if(len(nums) == 1):
            return nums[0]
        return max(simple_rob(nums[1:]), simple_rob(nums[:-1]))