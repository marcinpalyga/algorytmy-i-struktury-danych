import random
s = [random.randint(-50, 50) for i in range(15)]
print(s)
biggest = s[0]
smallest = s[0]
def findMinMax():
    global smallest, biggest
    if len(s) == 2:
        print(f"Biggest value in that sequence is {biggest}, smallest values is {smallest}")
    else:    
        if s[1] > s[0]:
            biggest = s[1]
            if s[2] <= biggest and s[2] >= smallest:
                s.pop(2)
                findMinMax()
            elif s[2] > biggest:
                biggest = s[2]
                s.pop(1)
                findMinMax()
            elif s[2] < smallest:
                smallest = s[2]
                s.pop(0)
                findMinMax()
        elif s[1] == s[0]:
            s.pop(1)
            findMinMax()
        else:
            smallest = s[1]
            if s[2] <= biggest and s[2] >= smallest:
                s.pop(2)
                findMinMax()
            elif s[2] > biggest:
                biggest = s[2]
                s.pop(0)
                findMinMax()
            elif s[2] < smallest:
                smallest = s[2]
                s.pop(1)
                findMinMax()
findMinMax()