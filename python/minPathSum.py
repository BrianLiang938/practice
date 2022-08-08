class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        out = grid
        for n in range(len(grid)):
            for m in range(len(grid[0])):
                if n == 0 and m == 0:
                    out[n][m] = grid[n][m]
                elif n == 0:
                    out[n][m] += grid[n][m - 1]
                elif m == 0:
                    out[n][m] += grid[n - 1][m]
                else:
                    out[n][m] += min(grid[n-1][m], grid[n][m-1])
        return out[-1][-1]