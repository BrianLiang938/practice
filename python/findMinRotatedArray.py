class Solution:
    def findMin(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1
        if nums[left] < nums[right]:
            return nums[0]
        while left <= right:
            pivot = left + (right - left) // 2
            if pivot == len(nums) - 1:
                return nums[pivot]
            if nums[pivot] < nums[pivot + 1] and nums[pivot] < nums[pivot - 1]:
                return nums[pivot]
            elif nums[pivot] >= nums[0]:
                left = pivot + 1
            elif nums[pivot] < nums[0]:
                right = pivot - 1
        return -1

def main():
    s = Solution()
    print(s.findMin([1, 2]))

if __name__ == "__main__":
    main()