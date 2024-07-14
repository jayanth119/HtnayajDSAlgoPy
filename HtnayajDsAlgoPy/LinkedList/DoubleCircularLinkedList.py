class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class DoubleCircularLinkedList:
    def __init__(self):
        self.root = None
        self.count = 0

    def insert_last(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            self.root.right = self.root
            self.root.left = self.root
        else:
            last_node = self.root.left
            last_node.right = new_node
            new_node.left = last_node
            new_node.right = self.root
            self.root.left = new_node
        self.count += 1

    def insert_first(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            self.root.right = self.root
            self.root.left = self.root
        else:
            first_node = self.root.right
            first_node.left = new_node
            new_node.right = first_node
            new_node.left = self.root
            self.root.right = new_node
            self.root = new_node
        self.count += 1

    def insert_between(self, data, i=0):
        if i > self.count or i < 0:
            print("Invalid position to insert.")
            return
        elif i == 0:
            self.insert_first(data)
        elif i == self.count:
            self.insert_last(data)
        else:
            temp = self.root
            for _ in range(i - 1):
                temp = temp.right
            new_node = Node(data)
            next_node = temp.right
            temp.right = new_node
            new_node.left = temp
            new_node.right = next_node
            next_node.left = new_node
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

    def delete_last(self):
        if self.root is None:
            print("List is empty.")
            return
        elif self.root.right == self.root:
            self.root = None
        else:
            last_node = self.root.left
            last_node.left.right = self.root
            self.root.left = last_node.left
        self.count -= 1

    def delete_first(self):
        if self.root is None:
            print("List is empty.")
            return
        elif self.root.right == self.root:
            self.root = None
        else:
            first_node = self.root.right
            first_node.right.left = self.root
            self.root.right = first_node.right
            self.root = first_node.right
        self.count -= 1

    def delete_between(self, i=-1):
        if i == -1:
            self.delete_last()
        elif i == 1:
            self.delete_first()
        elif i > self.count:
            print("Invalid position to delete.")
        else:
            temp = self.root
            for _ in range(i - 1):
                temp = temp.right
            delete_node = temp.right
            next_node = delete_node.right
            temp.right = next_node
            next_node.left = temp
            self.count -= 1
            return delete_node.data

    def delete(self, i=-1):
        if i == -1:
            self.delete_last()
        elif i == 1:
            self.delete_first()
        elif 1 < i <= self.count:
            return self.delete_between(i)
        else:
            print("Invalid position to delete.")

    def display(self):
        if self.root is None:
            print("List is empty.")
        else:
            temp = self.root
            while True:
                print(temp.data, end=" -> ")
                temp = temp.right
                if temp == self.root:
                    break
            print()

    def total_nodes(self):
        return self.count


