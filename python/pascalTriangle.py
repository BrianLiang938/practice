class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = [[0] * (numRows + 1) for j in range(numRows)]
        output[0] = [1]
        for n in range(numRows - 1):
            temp = [0] * (n + 2)
            temp[0] = 1
            temp[n + 1] = 1
            for i in range(n):
                temp[i + 1] = output[n][i] + output[n][i + 1]
            output[n + 1] = temp
        return output