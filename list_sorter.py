import random

def insertion_sort(arr):
  
    for i in range(1, len(arr)):
  
        key = arr[i]
  
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key

def selection_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):
            if(lst[j] < lst[min]):
                min = j
        lst[i], lst[min] = lst[min], lst[i]



# HEAP SORT

def heap_sort(arr):
    n = len(arr)
  
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
  
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] 
        heapify(arr, i, 0)

def heapify(arr, n, i):
    largest = i  
    l = 2 * i + 1   
    r = 2 * i + 2    
  
    if l < n and arr[i] < arr[l]:
        largest = l
  
    if r < n and arr[largest] < arr[r]:
        largest = r
  
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i] 

        heapify(arr, n, largest)


# MERGE SORT

def merge_sort(arr, l, r):
    if l < r:
        m = l+(r-l)//2
 
        merge_sort(arr, l, m)
        merge_sort(arr, m+1, r)
        merge(arr, l, m, r)

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    L = [0] * (n1)
    R = [0] * (n2)
 
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    i = 0     
    j = 0     
    k = l     
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# QUICK SORT

def quick_sort_lastpivot(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)

        quick_sort_lastpivot(arr, low, pi-1)
        quick_sort_lastpivot(arr, pi+1, high)


def quick_sort_randompivot(arr, start , stop):
    if(start < stop):
         
        pivotindex = partitionrand(arr,\
                             start, stop)
         
        quick_sort_randompivot(arr , start , pivotindex-1)
        quick_sort_randompivot(arr, pivotindex + 1, stop)

def quick_sort_midpivot(arr, start , stop):
    if(start < stop):
         
        pivotindex = partitionmid(arr,\
                             start, stop)
         
        quick_sort_midpivot(arr , start , pivotindex-1)
        quick_sort_midpivot(arr, pivotindex + 1, stop)
 
def partitionrand(arr , start, stop):
 
    randpivot = random.randrange(start, stop)

    arr[start], arr[randpivot] = \
        arr[randpivot], arr[start]
    return partition(arr, start, stop)

def partitionmid(arr , start, stop):
 
    pivot = int((start + stop)/2)

    arr[start], arr[pivot] = \
        arr[pivot], arr[start]
    return partition(arr, start, stop)

def partition(arr,start,stop):
    pivot = start
     
    i = start + 1
     
    for j in range(start + 1, stop + 1):
         
        if arr[j] <= arr[pivot]:
            arr[i] , arr[j] = arr[j] , arr[i]
            i = i + 1
    arr[pivot] , arr[i - 1] =\
            arr[i - 1] , arr[pivot]
    pivot = i - 1
    return (pivot)