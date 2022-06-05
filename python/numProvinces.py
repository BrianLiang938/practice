class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        sum = 0
        visited = [0] * len(isConnected)
        for x in range(len(isConnected)):
            if visited[x] == 0:
                self.dfs(isConnected, visited, x)
                sum += 1
        return sum

    def dfs(self, isConnected, visited, i):
        for j in range(len(isConnected)):
            if isConnected[i][j] == 1 and visited[j] == 0:
                visited[j] = 1
                self.dfs(isConnected, visited, j)

