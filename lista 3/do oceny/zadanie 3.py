def sumOfEl(n):
    summation = 0
    array = [[i+j+1 for i in range(n)] for j in range(n)]
    print(array)
    for i in range(n):
        for j in range(n):
            summation += array[i][j]
    return summation
print(sumOfEl(7))

