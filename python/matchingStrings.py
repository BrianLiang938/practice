def matchingStrings(strings, queries):
    strMap = {}
    for str in strings:
        if str not in strMap:
            strMap[str] = 1
        else:
            strMap[str] += 1
    out = [0] * len(queries)
    count = 0
    for str in queries:
        if str in strMap:
            out[count] = strMap[str]
        count += 1
    return out