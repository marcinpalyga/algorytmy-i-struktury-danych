import random
import tracemalloc

def findbiggest(s):
    if len(s) == 1:
        return s[0]
    while len(s) > 1:
        if s[0] >= s[1]:
            s.pop(1)
            return findbiggest(s)
        else:
            s.pop(0)
            return findbiggest(s)

tracemalloc.start()

s = [random.randint(-50, 50) for i in range(15)]
print(f"{s}, Largest element is {findbiggest(s)}")

current, peak = tracemalloc.get_traced_memory()

print(f"Memory allocated is {peak/1024:.2f}kB")
