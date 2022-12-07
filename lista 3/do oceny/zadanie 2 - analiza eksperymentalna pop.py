import random
import time

indexes = [i for i in range(50)]
A = [i for i in indexes]
times = [[0 for i in indexes] for j in indexes]

for j in indexes:
    for i in indexes:
        start = time.process_time_ns()
        A.pop(i)
        stop = time.process_time_ns()

        A.insert(i, random.randint(-50,50))
        times[i][j] = stop-start

avg = [sum(times[i])/len(indexes) for i in indexes]

import matplotlib.pyplot as plt
plt.scatter(indexes, avg)
plt.show()