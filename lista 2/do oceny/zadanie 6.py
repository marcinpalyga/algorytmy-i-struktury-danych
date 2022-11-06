import os

paths = []

def find(path, filename):
    if os.path.isdir(path):
        for file in os.listdir(path):
            if  file == filename:
                paths.append(os.path.join(path, file))
            else:
                childpath = os.path.join(path, file)
                find(childpath, filename)
    return paths

print(find("C:\\Users\\marci\\Desktop\\studia\\3 semestr\\algorytmy", "plik.txt"))