def swim(arr, k):
    while k > 1 and less(arr, int(k/2), k):
        exchange(arr, k, int(k/2))
        k = int(k/2)

def sink(arr, k, N):
    while 2*k <= N:
        j = 2*k
        if j < N and less(arr, j, j+1):
            j += 1
        if less(arr, j, k):
            break
        exchange(arr, k, j)
        k = j

def exchange(arr, m, n):
    arr[m-1], arr[n-1] = arr[n-1], arr[m-1]

def less(arr, m, n):
    if arr[m-1] < arr[n-1]:
        return True
    return False

def heap_sort(arr):
    #First we bring the array into heap order
    N = len(arr)
    for k in range(int(N/2), 0, -1):
        sink(arr, k, N)
    #And then we continuously get the max value and put it at the end
    while N > 1:
        exchange(arr, 1, N)
        N -= 1
        sink(arr, 1, N)  

import random
arr = []
for _ in range(100):
    arr.append(random.randint(1,100))
print(arr)

heap_sort(arr)
print(arr)