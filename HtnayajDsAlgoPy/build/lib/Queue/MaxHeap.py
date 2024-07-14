import numpy as np

class Heapers:
    def heapify(self, arr, n, index):
        try:
            lt = 2 * index + 1
            rt = 2 * index + 2
            largest = index
            if lt < n and arr[lt] > arr[largest]:
                largest = lt
            if rt < n and arr[rt] > arr[largest]:
                largest = rt
            if largest != index:
                arr[index], arr[largest] = arr[largest], arr[index]
                self.heapify(arr, n, largest)
        except IndexError as e:
            print(f"Error: {e}")
    
    def buildHeap(self, arr):
        try:
            n = len(arr)
            for i in range((n - 2) // 2, -1, -1):
                self.heapify(arr, n, i)
        except Exception as e:
            print(f"Error: {e}")
    
    def HeapSort(self, arr):
        try:
            n = len(arr)
            self.buildHeap(arr)
            for i in range(n - 1, 0, -1):
                arr[i], arr[0] = arr[0], arr[i]
                self.heapify(arr, i, 0)
            print("Sorted array:", arr)
        except Exception as e:
            print(f"Error: {e}")
    


