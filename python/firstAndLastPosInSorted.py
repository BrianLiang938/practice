class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        i = -1
        if len(nums) == 0:
            return [-1, -1]
        while left <= right:
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                i = pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        if i == -1:
            return [-1, -1]
        else:
            high = low = i
            while low >= 0:
                if nums[low] != target:
                    low = low + 1
                    break
                else:
                    low -= 1
            if low < 0:
                low = 0
            while high <= len(nums) - 1:
                if nums[high] != target:
                    high = high - 1
                    break
                else:
                    high += 1
            if high > len(nums) - 1:
                high = len(nums) - 1
            return [low,high]
