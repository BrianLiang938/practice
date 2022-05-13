class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        calculated = {}
        for n in range(len(numbers)):
            if numbers[n] in calculated:
                output = [calculated[numbers[n]] + 1, n + 1]
                return output
            else:
                calculated[target - numbers[n]] = n


        