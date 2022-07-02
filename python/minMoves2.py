class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        avg = median(nums)
        out = 0
        for num in nums:
            if num > avg:
                out += num - avg
            else:
                out += avg - num
        return int(out)