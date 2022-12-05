def Matrix_sum(A):
    """Function calculates the sum of all elements in a square Matrix n*n"""

    if type(A) is not list:         raise TypeError('argument is not a list')

    summation = 0
    for i in range(len(A)):
        if type(A[i]) is not list:  raise TypeError('argument is not a matrix')
        if len(A) != len(A[i]):     raise IndexError('argument is not n*n matrix')

        for j in range(len(A[i])):
            summation += A[i][j]
    
    return summation

A = [[2,2], [3,3,3]]

print(Matrix_sum(A))
