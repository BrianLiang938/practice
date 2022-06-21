class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix[0])
        m = len(matrix)
        i = 0
        mini = min(n,m)
        out = []
        while i <= mini:
            for j in range(n):
                out.append(matrix[(i/2)][j])
            for k in range(m):
                out.append(matrix[k][n - 1 - (i/2)])
            for j in range(n - 1, i - 1, -1):
                out.append(matrix[m - 1 - (i / 2)][j])
            for k in range(m - 1, i + 1, -1):
                out.append(matrix[k][(i/2)])