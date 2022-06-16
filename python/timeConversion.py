def timeConversion(s):
    if s[-2:] == "PM":
        i = str(int(s[:2]) + 12)
        if i == "24":
            return "12" + s[2:-2]
        return i + s[2:-2]
    else:
        if s[:2] == "12":
            return "00" + s[2:-2]
        return s[:-2]
    