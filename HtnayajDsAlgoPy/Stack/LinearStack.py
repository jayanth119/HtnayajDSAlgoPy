class LinearStack:
    """ Stack data structure based on first in last out (FILO) """

    def __init__(self, size):
        self.data = [-1] * size  # Initialize with placeholders
        self.size = size
        self.top = -1

    def push(self, data):
        try:
            if self.top == self.size - 1:
                raise Exception("Stack Overflow: Cannot push into a full stack")
            self.top += 1
            self.data[self.top] = data
        except Exception as e:
            print(e)

    def pop(self):
        try:
            if self.top == -1:
                raise Exception("Stack Underflow: Cannot pop from an empty stack")
            popped_item = self.data[self.top]
            self.top -= 1
            return popped_item
        except Exception as e:
            print(e)
            return -1  # Return a default value indicating failure

    def display(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            for i in range(self.top, -1, -1):
                print(self.data[i])

    def peek(self):
        if self.top == -1:
            return -1
        return self.data[self.top]

    def IsEmpty(self):
        return self.top == -1

    def IsFull(self):
        return self.top == self.size - 1

if __name__ == "__main__":
    try:
        a = LinearStack(4)
        print("Is stack full?", a.IsFull())
        print("Is stack empty?", a.IsEmpty())
        
        a.push(1)
        a.push(2)
        a.push(3)
        a.push(4)
        a.display()
        
        print("Is stack full?", a.IsFull())
        print("Is stack empty?", a.IsEmpty())
        
        # Attempting to push into a full stack
        a.push(5)

        # Attempting to pop from a non-empty stack
        popped_value = a.pop()
        print("Popped value:", popped_value)

        # Popping all elements
        while not a.IsEmpty():
            a.pop()

        # Attempting to pop from an empty stack
        a.pop()

    except Exception as e:
        print("Exception occurred:", e)
