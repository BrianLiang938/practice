class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        r = len(matrix)
        c = len(matrix[0])
        right = r * c - 1
        while left <= right:
            pivot = left + int((right - left) / 2)
            if matrix[int(pivot / c)][pivot % c] == target:
                return 1
            if matrix[int(pivot / c)][pivot % c] < target:
                left = pivot + 1
            elif matrix[int(pivot / c)][pivot % c] > target:
                right = pivot - 1
            
        return 0