def multiplying(m, n):
    if n == 1:  return m

    return m + multiplying(m, n-1)

print(multiplying(24, 34))
print(24 * 34)