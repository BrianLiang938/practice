class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        val = image[sr][sc]
        if val == newColor: return image
        def dfs(r, c):
            if image[r][c] == val:
                image[r][c] = newColor
                if r > 0:
                    dfs(r - 1, c)
                if r < len(image) - 1:
                    dfs(r + 1, c)
                if c > 0:
                    dfs(r, c - 1)
                if c < len(image[0]) - 1:
                    dfs(r, c + 1)
        dfs(sr, sc)
        return image