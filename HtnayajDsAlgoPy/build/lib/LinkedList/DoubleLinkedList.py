class LinkedListException(Exception):
    pass

class EmptyListException(LinkedListException):
    pass

class InvalidIndexException(LinkedListException):
    pass

class Node:
    def __init__(self, data):
        self.data = data
        self.LNode = None
        self.RNode = None

class DoubleLinkedList:
    def __init__(self):
        self.root = None
        self.count = 0

    def insert_last(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            temp = self.root
            while temp.RNode:
                temp = temp.RNode
            new = Node(data)
            new.LNode = temp
            temp.RNode = new
        self.count += 1

    def insert_first(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            new_node.RNode = self.root
            self.root.LNode = new_node
            self.root = new_node
        self.count += 1

    def insert_between(self, data, i=0):
        if i > self.count or i < 0:
            raise InvalidIndexException("Invalid index to insert")
        elif i == self.count:
            self.insert_last(data)
        elif i == 0:
            self.insert_first(data)
        else:
            temp = self.root
            for _ in range(i - 1):
                temp = temp.RNode
            new_node = Node(data)
            new_node.RNode = temp.RNode
            if temp.RNode:
                temp.RNode.LNode = new_node
            new_node.LNode = temp
            temp.RNode = new_node
            self.count += 1

    def insert(self, data, place=-1):
        if place == -1:
            self.insert_last(data)
        elif place == 1:
            self.insert_first(data)
        elif 1 < place <= self.count:
            self.insert_between(data, place)
        else:
            raise InvalidIndexException("Invalid place to insert")

    def delete_first(self):
        if self.root is None:
            raise EmptyListException("Cannot delete from an empty list")
        data = self.root.data
        self.root = self.root.RNode
        if self.root:
            self.root.LNode = None
        self.count -= 1
        return data

    def delete_last(self):
        if self.root is None:
            raise EmptyListException("Cannot delete from an empty list")
        if self.root.RNode is None:
            data = self.root.data
            self.root = None
        else:
            temp = self.root
            while temp.RNode.RNode:
                temp = temp.RNode
            data = temp.RNode.data
            temp.RNode = None
        self.count -= 1
        return data

    def delete_between(self, i=-1):
        if i == -1:
            return self.delete_last()
        elif i == 1:
            return self.delete_first()
        elif i > self.count or i < 1:
            raise InvalidIndexException("Invalid index to delete")
        else:
            temp = self.root
            for _ in range(i - 1):
                temp = temp.RNode
            data = temp.RNode.data
            temp.RNode = temp.RNode.RNode
            if temp.RNode:
                temp.RNode.LNode = temp
            self.count -= 1
            return data

    def delete(self, i=-1):
        if i == -1:
            return self.delete_last()
        elif i == 1:
            return self.delete_first()
        elif 1 < i <= self.count:
            return self.delete_between(i)
        else:
            raise InvalidIndexException("Invalid index to delete")

    def display(self):
        if self.root is None:
            print("The list is empty.")
            return
        temp = self.root
        while temp:
            print(temp.data, end=" -> ")
            if temp.RNode is None:
                print("null")
            temp = temp.RNode

    def total_nodes(self):
        return self.count
