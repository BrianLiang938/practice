def diagonalDifference(arr):
    left = right = 0
    for n in range(len(arr)):
        left += arr[n][n]
        right += arr[n][len(arr) - (n + 1)]
    return abs(left - right)