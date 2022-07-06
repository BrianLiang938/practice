class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numList = set(nums)
        out = 1
        curr = 1
        num = -1
        for n in numList:
            if n - 1 not in numList:
                curr = 1
                num = n
                while num + 1 in numList:
                    curr += 1
                    num += 1
                    out = max(out, curr)
        return out