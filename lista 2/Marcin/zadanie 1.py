import random
s = [random.randint(-50, 50) for i in range(15)]
print(s)
def findbiggest():
    if len(s) == 1:
        print(f"Biggest value of that sequence is {s[0]}")
    while len(s) > 1:
        if s[0] >= s[1]:
            s.pop(1)
            findbiggest()
        else:
            s.pop(0)
            findbiggest()

findbiggest()