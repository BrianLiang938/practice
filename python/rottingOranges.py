class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        output = grid
        visited = set()
        from collections import deque
        q = deque()
        for n in range(len(grid)):
            for m in range(len(grid[0])):
                if grid[n][m] == 2:
                    output[n][m] = 0
                    q.append((n, m))
                    visited.add((n, m))
        while q:
            x,y = q.popleft()
            for dirr in [(1,0), (-1,0), (0,1), (0,-1)]:
                newX, newY = x+dirr[0], y+dirr[1]
                if newX >= 0 and newX <= len(output)-1 and newY >= 0 and newY <= len(output[0])-1 and (newX, newY) not in visited and grid[newX][newY] != 0:
                        output[newX][newY] = output[x][y] + 1
                        visited.add((newX, newY))
                        q.append((newX, newY))
        print(output)
        for n in range(len(grid)):
            for m in range(len(grid[0])):
                if grid[n][m] == 1 and (n, m) not in visited:
                    return -1
        return max(map(max, output))

def main():
    s = Solution()
    mat = [[2,1,1],[0,1,1],[1,0,1]]
    print(s.orangesRotting(mat))

if __name__ == "__main__":
    main()