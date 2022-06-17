def lonelyinteger(a):
    curr = []
    for num in a:
        if num not in curr:
            curr.append(num)
        else:
            curr.remove(num)
    return curr[0]