def countingValleys(steps, path):
    out = 0
    height = 0
    for c in path:
        if c == "U":
            height += 1
            if height == 0:
                out += 1
        elif c == "D":
            height -= 1
    return out