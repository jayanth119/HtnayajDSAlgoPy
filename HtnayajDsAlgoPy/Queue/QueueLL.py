class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueLList:
    """Queue implementation using Linked List"""

    def __init__(self, size):
        self.size = size
        self.root = None
        self.front = None
        self.rear = None
        self.count = 0

    def Enqueue(self, data):
        try:
            if self.isfull():
                raise Exception("QueueLList is full")
            new_node = Node(data)
            if self.root is None:
                self.root = new_node
                self.front = self.root
                self.rear = self.root
            else:
                self.rear.next = new_node
                self.rear = new_node
            self.count += 1
        except Exception as e:
            print(f"Enqueue Error: {e}")

    def Dequeue(self):
        try:
            if self.isempty():
                raise Exception("QueueLList is empty")
            if self.front == self.rear:
                self.front = None
                self.rear = None
            else:
                self.front = self.front.next
            self.count -= 1
        except Exception as e:
            print(f"Dequeue Error: {e}")

    def isempty(self):
        return self.root is None

    def isfull(self):
        return self.count == self.size

    def display(self):
        try:
            if self.isempty():
                print("QueueLList is empty")
                return
            current = self.front
            while current:
                print(current.data, end=" -> ")
                current = current.next
            print("None")
        except Exception as e:
            print(f"Display Error: {e}")

    def size(self):
        return self.count


# # Example usage:
# if __name__ == "__main__":
#     queue = QueueLList(5)
#     queue.Enqueue(10)
#     queue.Enqueue(20)
#     queue.Enqueue(15)
#     queue.display()  # Output: 10 -> 20 -> 15 -> None
#     queue.Dequeue()
#     queue.display()  # Output: 20 -> 15 -> None
#     print("Queue size:", queue.size())  # Output: Queue size: 2
#     print("Is queue empty?", queue.isempty())  # Output: Is queue empty? False
#     print("Is queue full?", queue.isfull())  # Output: Is queue full? False
#     queue.Enqueue(5)
#     queue.Enqueue(25)
#     queue.Enqueue(30)  # Trying to enqueue more than capacity
#     queue.display()  # Output: 20 -> 15 -> 5 -> 25 -> 30 -> None
