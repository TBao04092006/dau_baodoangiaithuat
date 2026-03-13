def arrangeCoins(n):
    row = 1
    while n >= row:
        n -= row
        row += 1
    return row - 1