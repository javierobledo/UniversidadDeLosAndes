def range_rec(n):
    if n == 0:
        return []
    return range_rec(n-1)+[n-1]