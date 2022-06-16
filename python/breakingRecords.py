def breakingRecords(scores):
    rec = [scores[0]] * 2
    out = [0] * 2
    for num in scores:
        if num < rec[0]:
            out[1] += 1
            rec[0] = num
        elif num > rec[1]:
            out[0] += 1
            rec[1] = num
    return out