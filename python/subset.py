class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first = 0, curr = []):
            if len(curr) == k:
                if curr[:] not in output:
                    output.append(curr[:])
                return
            for i in range(first,n):
                curr.append(nums[i])
                backtrack(i + 1, curr)
                curr.pop()
        output = []
        n = len(nums)
        for k in range(n+1):
            backtrack()
        return output