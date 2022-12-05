def sumOfEl(n):
    sum = 0
    array = [[i+j+1 for i in range(n)] for j in range(n)]
    print(array)
    for i in range(n):
        for j in range(n):
            print(array[i][j])
            sum += array[i][j]
    return sum
print(sumOfEl(7))

