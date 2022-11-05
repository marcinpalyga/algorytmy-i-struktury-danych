import os

paths = []

def find(path, filename):
    if os.path.isdir(path):
        for element in os.listdir(path):
            file = os.path.basename(element)
            if  file == filename:
                paths.append(os.path.join(path, file))
            else:
                childpath = os.path.join(path, element)
                print(childpath)
                find(childpath, filename)
    return paths

print(find("C:\\Users\\marci\\Desktop\\studia\\3 semestr\\algorytmy", "plik.txt"))