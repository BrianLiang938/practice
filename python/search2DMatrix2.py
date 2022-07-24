class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == None or len(matrix) < 1 or len(matrix[0]) < 1:
            return False
        col = len(matrix[0]) - 1
        row = 0
        while col >= 0 and row <= len(matrix) - 1:
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                col -= 1
            elif target > matrix[row][col]:
                row += 1
        return False