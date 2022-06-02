class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1
        #queue of nodes to visit
        q = [(0, 0, 1)]
        #denotes visited
        grid[0][0] = 1
        for i, j, d in q:
            if i == n-1 and j == n-1:
                return d
            #checks for 8 directional movement and conditions to move in that direction
            for x, y in ((i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)):
                if 0 <= x < n and 0 <= y < n and grid[x][y] == 0:
                    grid[x][y] = 1
                    q.append((x, y, d + 1))
        return -1


def main():
    s = Solution()
    grid = [[0,0,0],[1,1,0],[1,1,0]]
    s.shortestPathBinaryMatrix(grid)
if __name__ == "__main__":
    main()