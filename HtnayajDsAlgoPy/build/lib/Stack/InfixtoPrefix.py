from LinearStack import LinearStack

class Prefix:
    def __init__(self):
        pass
    
    def isoperator(self, a):
        operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        return a in operators
    
    def precedence(self, a):
        operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        return operators.get(a, 0)
    
    def InfixtoPrefix(self, infix):
        infix = infix[::-1]  # Reverse the infix expression
        stack = LinearStack(len(infix))
        ans = ""
        
        try:
            for i in range(len(infix)):
                if infix[i] == ')':
                    stack.push(infix[i])
                elif infix[i] == '(':
                    while not stack.IsEmpty() and stack.peek() != ')':
                        ans += stack.pop()
                    if not stack.IsEmpty() and stack.peek() == ')':
                        stack.pop()  # Remove the ')' from stack
                elif self.isoperator(infix[i]):
                    while (not stack.IsEmpty() and
                           self.precedence(infix[i]) < self.precedence(stack.peek())):
                        ans += stack.pop()
                    stack.push(infix[i])
                else:
                    ans += infix[i]
            
            while not stack.IsEmpty():
                ans += stack.pop()
            
            # Reverse the final prefix expression to get the correct order
            ans = ans[::-1]

            print("The prefix expression is:", ans)
        
        except Exception as e:
            print(f"Error occurred: {e}")

# # Example usage:
# if __name__ == "__main__":
#     infix_expression = input("Enter infix expression: ")
#     prefix_converter = Prefix()
#     prefix_converter.InfixtoPrefix(infix_expression)
