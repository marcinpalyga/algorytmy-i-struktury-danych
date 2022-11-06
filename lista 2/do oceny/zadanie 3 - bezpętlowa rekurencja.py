def minmax_rec(S):
    if len(S) == 2:
        if S[0] > S[1]:     return [S[0], S[1]]
        else:               return [S[1], S[0]]

    first_el, next_el = S[0], minmax_rec(S[1:])
    print(next_el)
    if first_el > next_el[0]:   return [first_el, next_el[1]]   #zwracanie wiekszego elementu z trzech ostatnich liczb
    if first_el < next_el[1]:   return [next_el[0], first_el]   #zwracanie mniejszego elementu z trzech ostatnich liczb
    else:                       return next_el                  #trzeci od konca jest mniejszy od najwiekszego i wiekszy od najmniejszego


import random

S = [random.randint(-20, 20) for i in range(random.randint(2, 20))]

print(S)
print(minmax_rec(S))
