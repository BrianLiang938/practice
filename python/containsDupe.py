import collections
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        output = set()
        for x in nums:
            output.add(x)
        return len(output) != len(nums)