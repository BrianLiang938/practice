def marsExploration(s):
    out = 0
    for i in range(len(s)):
        if i % 3 == 1:
            if s[i] != "O":
                out += 1
        elif s[i] != "S":
            out += 1
    return out
