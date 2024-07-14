class LinkedListException(Exception):
    pass

class EmptyListException(LinkedListException):
    pass

class InvalidIndexException(LinkedListException):
    pass

class Node:
    def __init__(self, data=None):
        self.data = data
        self.Node = None

class LinkedList:
    def __init__(self):
        self.root = None
        self.count = 0 

    def insert_last(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            current_node = self.root
            while current_node.Node:
                current_node = current_node.Node
            current_node.Node = Node(data)
        self.count += 1 

    def insert_first(self, data):
        new_node = Node(data)
        new_node.Node = self.root
        self.root = new_node
        self.count += 1 

    def insert_between(self, data, i=0):
        if i > self.count:
            raise InvalidIndexException("Invalid index to insert")
        elif i == self.count:
            self.insert_last(data)
        elif i == 0:
            self.insert_first(data)
        else:
            temp = self.root
            for _ in range(i - 1):
                if temp is None:
                    raise InvalidIndexException("Invalid index to insert")
                temp = temp.Node
            new_node = Node(data)
            new_node.Node = temp.Node
            temp.Node = new_node
            self.count += 1

    def insert(self, data, place=-1):
        if place == -1:
            self.insert_last(data)
        elif place == 1:
            self.insert_first(data)
        elif 1 < place < self.count:
            self.insert_between(data, place)
        else:
            raise InvalidIndexException("Invalid place to insert")

    def delete_first(self):
        if self.root is None:
            raise EmptyListException("Cannot delete from an empty list")
        c = self.root.data
        self.root = self.root.Node
        self.count -= 1
        return c

    def delete_last(self):
        if self.root is None:
            raise EmptyListException("Cannot delete from an empty list")
        if self.root.Node is None:
            c = self.root.data
            self.root = None
            self.count -= 1
            return c
        p = self.root
        while p.Node and p.Node.Node:
            p = p.Node
        c = p.Node.data
        p.Node = None
        self.count -= 1
        return c

    def delete_between(self, i=-1):
        if i == -1:
            return self.delete_last()
        if i == 1:
            return self.delete_first()
        if i > self.count:
            raise InvalidIndexException("Invalid index to delete")
        p = self.root
        for _ in range(i - 2):
            p = p.Node
        q = p.Node
        c = q.data
        p.Node = q.Node
        self.count -= 1
        return c

    def delete(self, i=-1):
        if i == -1:
            return self.delete_last()
        elif i == 1:
            return self.delete_first()
        elif 1 < i < self.count:
            return self.delete_between(i)
        else:
            raise InvalidIndexException("Invalid index to delete")

    def display(self):
        temp = self.root
        if temp is None:
            print("Linked list is empty")
        while temp:
            print(temp.data, end=" -> ")
            if temp.Node is None:
                print("null")
            temp = temp.Node

    def total_nodes(self):
        return self.count
