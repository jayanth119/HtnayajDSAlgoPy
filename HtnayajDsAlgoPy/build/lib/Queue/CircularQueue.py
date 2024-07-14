class CQueueArray:
    """Circular Queue implementation using arrays."""
    def __init__(self, arg):
        self.data = [0] * arg  # Initialize array with zeros
        self.count = 0         # Number of elements in the queue
        self.size = arg        # Maximum size of the queue
        self.front = -1        # Pointer to front of the queue
        self.rear = -1         # Pointer to rear of the queue

    def Enqueue(self, data):
        try:
            if self.isFull():
                raise Exception("Queue is full")
            else:
                if self.front == -1:  # Empty queue
                    self.front = 0
                self.rear = (self.rear + 1) % self.size
                self.data[self.rear] = data
                self.count += 1
        except Exception as e:
            print(f"Error: {e}")

    def Dequeue(self):
        try:
            if self.isEmpty():
                raise Exception("Queue is empty")
            else:
                item = self.data[self.front]
                self.front = (self.front + 1) % self.size
                self.count -= 1
                if self.isEmpty():  # Reset pointers if queue becomes empty
                    self.front = -1
                    self.rear = -1
                return item
        except Exception as e:
            print(f"Error: {e}")
            return None

    def display(self):
        try:
            if self.isEmpty():
                print("Queue is empty")
            else:
                p = self.front
                q = self.rear
                while p <= q:
                    print(self.data[p], end=" ")
                    p += 1
                print()
        except Exception as e:
            print(f"Error: {e}")

    def Peek(self):
        try:
            if self.isEmpty():
                raise Exception("Queue is empty")
            else:
                return self.data[self.front]
        except Exception as e:
            print(f"Error: {e}")
            return None

    def Size(self):
        return self.count

    def Clear(self):
        self.front = -1
        self.rear = -1
        self.count = 0
        self.data = [0] * self.size

    def isFull(self):
        return self.count == self.size

    def isEmpty(self):
        return self.count == 0

    def Search(self, key):
        try:
            if self.isEmpty():
                raise Exception("Queue is empty")
            else:
                p = self.front
                q = self.rear
                while p <= q:
                    if self.data[p] == key:
                        return True
                    p += 1
                return False
        except Exception as e:
            print(f"Error: {e}")
            return False

    def __iter__(self):
        self._iter_index = self.front
        return self

    def __next__(self):
        if self._iter_index > self.rear:
            raise StopIteration
        else:
            value = self.data[self._iter_index]
            self._iter_index += 1
            return value

    def isFull(self):
        return self.count == self.size

    def isEmpty(self):
        return self.count == 0
