def power(x, n):
    """Compute the value x**n for integer n."""
    if n == 0:
       return 1
    else:
       return x*power(x, n-1)

print('Ślad rekurencyjny funkcji power dla 2^5:')
print('power(2,5)')
print('power(2,4)')
print('power(2,3)')
print('power(2,2)')
print('power(2,1)')
print('power(2,0)')
print('return 1')
print('return 2*1')
print('return 2*2')
print('return 2*4')
print('return 2*8')
print('return 2*16')