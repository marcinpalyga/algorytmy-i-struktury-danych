import time

sizes = [1000,25,50,100]
array = [i for i in range(1000)]
time0 = []
time10 = []
time25 = []
time50 = []
time100 = []
for i in sizes:
    start = time.process_time()
    array.pop(0)
    end = time.process_time()
    result = end - start
    time0.append(result)

    start = time.process_time()
    array.pop(10)
    end = time.process_time()
    result = end - start
    time10.append(start)

    start = time.process_time_ns()
    array.pop(25)
    end = time.process_time_ns()
    result = end - start
    time25.append(result)

    start = time.process_time_ns()
    array.pop(50)
    end = time.process_time_ns()
    result = end - start
    time50.append(result)

    start = time.process_time_ns()
    array.pop(100)
    end = time.process_time_ns()
    result = end - start
    time100.append(result)
print(time0)
print(time10)
print(time25)
print(time50)
print(time100)
