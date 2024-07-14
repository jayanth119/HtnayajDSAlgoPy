import numpy as np


def Merge(arr, low, high, n, mid):
    b = np.zeros(n, dtype=int)
    k = low
    i = low
    j = mid + 1
    while i <= mid and j <= high:
        if arr[i] < arr[j]:
            b[k] = arr[i]
            k += 1
            i += 1
        else:
            b[k] = arr[j]
            k += 1
            j += 1
    while i <= mid:
        b[k] = arr[i]
        i += 1
        k += 1
    while j <= high:
        b[k] = arr[j]
        j += 1
        k += 1
    arr[low:high + 1] = b[low:high + 1]

def MergeSort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        MergeSort(arr, low, mid)
        MergeSort(arr, mid + 1, high)
        Merge(arr, low, high, len(arr), mid)