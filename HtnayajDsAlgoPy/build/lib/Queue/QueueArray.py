import numpy as np
from HtnayajDsAlgoPy.Sorting import MergeSort

class QueueArray:
    """Queue implementation using NumPy array"""

    def __init__(self, size):
        self.data = np.zeros(size, dtype=int)
        self.count = 0
        self.size = size
        self.front = -1
        self.rear = -1

    def Enqueue(self, data):
        try:
            if self.rear == -1:
                self.rear += 1
                self.front += 1
                self.data[self.rear] = data
                self.count += 1
                return
            elif self.rear == self.size - 1:
                raise Exception("Queue is full")
            else:
                self.rear += 1
                self.data[self.rear] = data
                self.count += 1
            MergeSort(self.data, 0, self.rear)
        except Exception as e:
            print(f"Enqueue Error: {e}")

    def isFull(self):
        return self.count == self.size

    def isEmpty(self):
        return self.front == -1

    def Dequeue(self):
        try:
            if self.front == -1 or self.front > self.rear:
                raise Exception("Queue is empty")
            elif self.front + 1 == self.size:
                c = self.data[self.front]
                self.count -= 1
                self.front = -1
                self.rear = -1
                return c
            self.count -= 1
            c = self.data[self.front]
            self.front += 1
            return c
        except Exception as e:
            print(f"Dequeue Error: {e}")

    def display(self):
        try:
            if self.isEmpty():
                print("Queue is empty")
                return
            print("Queue:", self.data[self.front:self.rear + 1])
        except Exception as e:
            print(f"Display Error: {e}")

    def size(self):
        return self.count


# Example usage:
# if __name__ == "__main__":
#     queue = QueueArray(5)
#     queue.Enqueue(10)
#     queue.Enqueue(20)
#     queue.Enqueue(15)
#     queue.display()  # Output: Queue: [10 15 20]
#     print("Dequeued:", queue.Dequeue())  # Output: Dequeued: 10
#     queue.display()  # Output: Queue: [15 20]
#     print("Queue size:", queue.size())  # Output: Queue size: 2
#     print("Is queue empty?", queue.isEmpty())  # Output: Is queue empty? False
#     print("Is queue full?", queue.isFull())  # Output: Is queue full? False
#     queue.Enqueue(5)
#     queue.Enqueue(25)
#     queue.Enqueue(30)  # Trying to enqueue more than capacity
#     queue.display()  # Output: Queue: [ 5 15 20 25 30] (after sorting)
