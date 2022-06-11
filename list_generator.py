import random

def const_list(listLength):
    return [1] * listLength

def random_list(listLength):
    arr = []

    for i in range(listLength):
        arr.append(random.randint(0, listLength))
    return arr

def ascending_list(listLength):
    arr = []

    for i in range(listLength):
        arr.append(i)

    return arr

def descending_list(listLength):
    arr = []

    for i in range(listLength):
        arr.append(listLength-1-i)
        
    return arr

def A_shape_list(listLength):
    arr = ascending_list(int(listLength/2))  
    arr.extend(descending_list(int(listLength/2)))
    return arr

def V_shape_list(listLength):  
    arr = descending_list(int(listLength/2))  
    arr.extend(ascending_list(int(listLength/2)))
    return arr