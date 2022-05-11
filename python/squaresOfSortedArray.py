class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        negative = 0
        output = []
        for x in range(len(nums)):
            if x >= 0:
                positive = x
                negative = x - 1
                break
        for x in range(len(nums)):
            if nums[positive] > -1 * nums[negative]:
                input = nums[negative] ** 2
                output.append(input)
                negative -= 1
            elif nums[positive] <= -1 * nums[negative]:
                input = nums[positive] ** 2
                output.append(input)
                positive += 1
        return output