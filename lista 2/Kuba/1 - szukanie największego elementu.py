import random
import tracemalloc


def largest_element(S, k=0):
    for n in range(0, len(S)-1):

        if S[n] <= S[n+1]:
            a, b = S[n], S[n+1]
            S[n+1], S[n] = a, b

    if k == len(S):     return S[0]
    else:               return largest_element(S, k+1)

tracemalloc.start()

S = [random.randint(-50, 50) for i in range(1, 31)]
print(S, '\nlargest element -->', largest_element(S))

current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print('This function has efficiency of O(n^2)')
print(f'Memory allocated: {peak/1024:.2f} kB')
