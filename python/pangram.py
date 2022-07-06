def pangrams(s):
    str = s.lower()
    out = True
    freq = [False] * 26
    for c in str:
        if c != ' ':
            freq[ord(c) - ord('a')] = True
    for n in range(len(freq)):
        out = out and freq[n]
    if out:
        return "pangram"
    else:
        return "not pangram"