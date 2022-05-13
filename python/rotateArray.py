class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        end = len(nums) - k
        right = nums[end: ]
        for n in range(end):
            nums[-(n + 1)] = nums[-(n + k + 1)]
        for i in range(len(right)):
            nums[i] = right[i]

def main():
    nums = [1,2,3,4,5,6,7]
    k = 3
    end = len(nums) - k
    right = nums[end: ]
    for n in range(end):
        nums[-(n + 1)] = nums[-(n + k + 1)]
    for i in range(len(right)):
        nums[i] = right[i]
    print(nums)


if __name__ == "__main__":
    main()