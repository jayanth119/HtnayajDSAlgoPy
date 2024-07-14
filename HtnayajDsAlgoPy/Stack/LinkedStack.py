class Node:
    def __init__(self, data):
        self.data = data
        self.Nxt = None


class StackLL:
    def __init__(self):
        self.root = None
        self.top = None
        self.count = -1

    def push(self, data):
        if self.root is None:
            new_node = Node(data)
            self.root = new_node
            self.top = new_node
            self.count = 0
        else:
            new_node = Node(data)
            new_node.Nxt = self.top
            self.top = new_node
            self.count += 1

    def pop(self):
        if self.count == -1:
            print("Stack Underflow: Cannot pop from an empty stack")
            return -1
        else:
            popped_data = self.top.data
            self.top = self.top.Nxt
            self.count -= 1
            if self.count == -1:
                self.root = None  # Reset root if stack becomes empty
            return popped_data

    def peek(self):
        if self.root is None:
            print("Stack is empty: Cannot peek")
            return -1
        return self.top.data

    def display(self):
        if self.root is None:
            print("Stack is empty")
        else:
            p = self.top
            while p is not None:
                print(p.data)
                p = p.Nxt

# # Example usage:
# if __name__ == "__main__":
#     try:
#         stack = StackLL()

#         print("Peek:", stack.peek())  # Should print "Stack is empty: Cannot peek"
#         print("Pop:", stack.pop())    # Should print "Stack Underflow: Cannot pop from an empty stack"

#         stack.push(1)
#         stack.push(2)
#         stack.push(3)

#         print("Peek after pushes:", stack.peek())  # Should print 3

#         print("Display stack:")
#         stack.display()  # Should print 3, 2, 1 from top to bottom

#         print("Pop:", stack.pop())  # Should print 3
#         print("Pop:", stack.pop())  # Should print 2

#         print("Peek after pops:", stack.peek())  # Should print 1

#         print("Display stack after pops:")
#         stack.display()  # Should print 1

#         print("Pop:", stack.pop())  # Should print 1
#         print("Pop:", stack.pop())  # Should print "Stack Underflow: Cannot pop from an empty stack"
    
#     except Exception as e:
#         print("Exception occurred:", e)
