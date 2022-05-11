class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        values = {}
        for x in range(len(nums)):
            if nums[x] in values:
                output = []
                output.append(x)
                output.append(nums.index(target - nums[x]))
                return output
            values[target - nums[x]] = x


def main():
    n = 1
    for x in range(n):
        print(x)

if __name__ == "__main__":
    main()