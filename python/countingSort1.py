def countingSort(arr):
    out = [0] * 100
    for num in arr:
        out[num] += 1
    return out