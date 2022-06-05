class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        if nums[0] < target:           
            while left <= right:
                pivot = left + (right - left) // 2
                if nums[pivot] == target:
                    return pivot
                if target < nums[pivot] or nums[pivot] < nums[0]:
                    right = pivot - 1
                else:
                    left = pivot + 1
            return -1
        elif nums[0] > target:
            while left <= right:
                pivot = left + (right - left) // 2
                if nums[pivot] == target:
                    return pivot
                if target > nums[pivot] or nums[pivot] > nums[-1]:
                    left = pivot + 1
                else:
                    right = pivot - 1
            return -1
        else:
            return 0
def main():
    s = Solution()
    print(s.search([4,5,6,7,0,1,2], 3))
if __name__ == "__main__":
    main()