class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.root = None
        self.count = 0

    def insert_last(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            new_node.next = self.root
        else:
            current_node = self.root
            while current_node.next != self.root:
                current_node = current_node.next
            current_node.next = new_node
            new_node.next = self.root
        self.count += 1

    def insert_first(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            new_node.next = self.root
        else:
            current_node = self.root
            while current_node.next != self.root:
                current_node = current_node.next
            new_node.next = self.root
            current_node.next = new_node
            self.root = new_node
        self.count += 1

    def insert_between(self, data, i=0):
        if i > self.count or i < 0:
            print("Invalid position to insert.")
            return
        elif i == self.count:
            self.insert_last(data)
        elif i == 0:
            self.insert_first(data)
        else:
            new_node = Node(data)
            current_node = self.root
            for _ in range(i - 1):
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node
            self.count += 1

    def insert(self, data, place=-1):
        if place == -1:
            self.insert_last(data)
        elif place == 1:
            self.insert_first(data)
        elif 1 < place < self.count:
            self.insert_between(data, place)
        else:
            print("Invalid position to insert.")

    def delete_first(self):
        if self.root is None:
            print("List is empty.")
            return -1
        elif self.root.next == self.root:
            deleted_data = self.root.data
            self.root = None
        else:
            current_node = self.root
            while current_node.next != self.root:
                current_node = current_node.next
            deleted_data = self.root.data
            current_node.next = self.root.next
            self.root = self.root.next
        self.count -= 1
        return deleted_data

    def delete_last(self):
        if self.root is None:
            print("List is empty.")
            return -1
        elif self.root.next == self.root:
            deleted_data = self.root.data
            self.root = None
        else:
            current_node = self.root
            while current_node.next.next != self.root:
                current_node = current_node.next
            deleted_data = current_node.next.data
            current_node.next = self.root
        self.count -= 1
        return deleted_data

    def delete_between(self, i=-1):
        if i == -1:
            return self.delete_last()
        elif i == 1:
            return self.delete_first()
        elif i > self.count:
            print("Invalid position to delete.")
            return -1
        else:
            current_node = self.root
            for _ in range(i - 2):
                current_node = current_node.next
            deleted_data = current_node.next.data
            current_node.next = current_node.next.next
            self.count -= 1
            return deleted_data

    def delete(self, i=-1):
        if i == -1:
            return self.delete_last()
        elif i == 1:
            return self.delete_first()
        elif 1 < i <= self.count:
            return self.delete_between(i)
        else:
            print("Invalid position to delete.")
            return -1

    def display(self):
        if self.root is None:
            print("Linked list is empty.")
            return
        current_node = self.root
        while True:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
            if current_node == self.root:
                break
        print()

    def total_nodes(self):
        return self.count


