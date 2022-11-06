def product(a,b):
    if b == 0:
        return 0
    else:
        return a+product(a, b-1)
print(product(5,1))