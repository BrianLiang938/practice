class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 99999
        nonzero = -1
        for n in range(len(nums)):
            if nums[n] == 0 and n < zero:
                zero = n
            else:
                nonzero = n
            if nonzero > zero:
                nums[zero] = nums[nonzero]
                nums[nonzero] = 0
                zero = nums.index(0)

