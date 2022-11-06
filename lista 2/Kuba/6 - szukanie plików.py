import os

paths = [] 

def find(path, filename):
    

    if os.path.isdir(path):
        for element in os.listdir(path):

            if  element == filename:
                paths.append(os.path.join(path, filename))
            else:
                new_path = os.path.join(path, element)
                find(new_path, filename)   

    return paths

print(find('/Users/jakubkempa/Downloads','IMG_9584.JPG'))