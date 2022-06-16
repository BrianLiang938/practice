def plusMinus(arr):
    p = z = n = sum = 0
    for nums in arr:
        if nums > 0:
            p += 1
        elif nums == 0:
            z += 1
        else:
            n += 1
        sum += 1
    print(p / sum)
    print(n / sum)
    print(z / sum)
    