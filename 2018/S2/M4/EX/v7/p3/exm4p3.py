def range_rec(m,n):
    if n <= m:
        return []
    return range_rec(m,n-1)+[n-1]