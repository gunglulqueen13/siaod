#task 1

str = "Hello, World!"
print(str)

#task 2

import random

arr = []
user_m = int(input())
user_n = int(input())
user_min_limit = int(input())
user_max_limit = int(input())

for i in range(user_m):
    arr_two = []
    for j in range(user_n):
        arr_two.append(random.randint(user_min_limit, user_max_limit))
    arr.append(arr_two)

print(arr)

#task 3

import math
import time

def selection_sort(): #сортировка выбором
    arr_sorted = []
    for m in range(len(arr)):
        alist = arr[m]
        for i in range(0, len(alist) - 1):
            smallest = i
            for j in range(i + 1, len(alist)):
                if alist[j] < alist[smallest]:
                    smallest = j
            alist[i], alist[smallest] = alist[smallest], alist[i]
        arr_sorted.append(alist)
    return arr_sorted

def insertion_sort(): #сортировка вставками
    arr_sorted = []
    for m in range(len(arr)):
        alist = arr[m]
        for i in range(1, len(alist)):
            temp = alist[i]
            j = i - 1
            while (j >= 0 and temp < alist[j]):
                alist[j + 1] = alist[j]
                j = j - 1
            alist[j + 1] = temp
        arr_sorted.append(alist)
    return arr_sorted

def bubble_sort(): #сортировка пузырьком
    arr_sorted = []
    for m in range(len(arr)):
        alist = arr[m]
        for i in range(len(alist) - 1, 0, -1):
            no_swap = True
            for j in range(0, i):
                if alist[j + 1] < alist[j]:
                    alist[j], alist[j + 1] = alist[j + 1], alist[j]
                    no_swap = False
            if no_swap:
                break
        arr_sorted.append(alist)
    return arr_sorted

def shell_sort(): #сортировка Шелла
    arr_sorted = []
    for m in range(len(arr)):
        alist = arr[m]
        n = len(alist)
        k = int(math.log2(n))
        interval = 2**k -1
        while interval > 0:
            for i in range(interval, n):
                temp = alist[i]
                j = i
                while j >= interval and alist[j - interval] > temp:
                    alist[j] = alist[j - interval]
                    j -= interval
                alist[j] = temp
            k -= 1
            interval = 2 ** k -1
        arr_sorted.append(alist)
    return arr_sorted
    
def partition(alist, start, end):
    pivot = alist[start]
    i = start + 1
    j = end - 1
 
    while True:
        while (i <= j and alist[i] <= pivot):
            i = i + 1
        while (i <= j and alist[j] >= pivot):
            j = j - 1
 
        if i <= j:
            alist[i], alist[j] = alist[j], alist[i]
        else:
            alist[start], alist[j] = alist[j], alist[start]
            return j

def quicksort(alist, start, end):
    if end - start > 1:
        p = partition(alist, start, end)
        quicksort(alist, start, p)
        quicksort(alist, p + 1, end)
 
 


def quick_sort():
    arr_sorted = []
    for m in range(len(arr)):
        alist = arr[m]
        quicksort(alist, 0, len(alist))
        arr_sorted.append(alist)
    return arr_sorted

def heapsort(alist):
    build_max_heap(alist)
    for i in range(len(alist) - 1, 0, -1):
        alist[0], alist[i] = alist[i], alist[0]
        max_heapify(alist, index=0, size=i)
 
 
def build_max_heap(alist):
    length = len(alist)
    start = (length - 2) // 2
    while start >= 0:
        max_heapify(alist, index=start, size=length)
        start = start - 1
 
def max_heapify(alist, index, size):
    l = 2 * index + 1
    r = 2 * index + 2
    if (l < size and alist[l] > alist[index]):
        largest = l
    else:
        largest = index
    if (r < size and alist[r] > alist[largest]):
        largest = r
    if (largest != index):
        alist[largest], alist[index] = alist[index], alist[largest]
        max_heapify(alist, largest, size)

def heap_sort():
    arr_sorted = []
    for m in range(len(arr)):
        alist = arr[m]
        heapsort(alist)
        arr_sorted.append(alist)
    return arr_sorted     



# Сортировка выбором.
start_time = time.time()
selection_sort()
print("--- {0} ms ---".format(round((time.time() - start_time)*1000)))

# Сортировка вставкой.
start_time = time.time()
insertion_sort()
print("--- {0} ms ---".format(round((time.time() - start_time)*1000)))

# Сортировка обменом. || Сортировка пузырьком.
start_time = time.time()
bubble_sort()
print("--- {0} ms ---".format(round((time.time() - start_time)*1000)))

# Сортировка Шелла.
start_time = time.time()
shell_sort()
print("--- {0} ms ---".format(round((time.time() - start_time)*1000)))

# Быстрая сортировка.
start_time = time.time()
quick_sort()
print("--- {0} ms ---".format(round((time.time() - start_time)*1000)))

# Турнирная сортировка.
start_time = time.time()
heap_sort()
print("--- {0} ms ---".format(round((time.time() - start_time)*1000)))






