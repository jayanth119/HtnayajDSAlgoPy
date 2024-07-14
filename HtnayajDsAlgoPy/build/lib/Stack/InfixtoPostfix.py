from LinearStack import LinearStack  # Assuming LinearStack is implemented correctly

class Infix:
    def __init__(self):
        pass
    
    def isoperator(self, a):
        operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        return a in operators
    
    def precedence(self, a):
        operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        return operators.get(a, 0)
    
    def InfixtoPostfix(self, infix):
        stack = LinearStack(len(infix))
        ans = ""
        
        try:
            for i in range(len(infix)):
                if infix[i] == '(':
                    stack.push(infix[i])
                elif infix[i] == ')':
                    while not stack.IsEmpty() and stack.peek() != '(':
                        ans += stack.pop()
                    if not stack.IsEmpty() and stack.peek() == '(':
                        stack.pop()  # Remove the '(' from stack
                elif self.isoperator(infix[i]):
                    while (not stack.IsEmpty() and
                           self.precedence(infix[i]) <= self.precedence(stack.peek())):
                        ans += stack.pop()
                    stack.push(infix[i])
                else:
                    ans += infix[i]
            
            while not stack.IsEmpty():
                ans += stack.pop()
            
            # Remove any remaining '(' from ans
            ans = ans.replace('(', '')

            print("The postfix expression is:", ans)
        
        except Exception as e:
            print(f"Error occurred: {e}")

# # Example usage:
# if __name__ == "__main__":
#     infix_expression = "a + b * (c ^ d - e) / f"
#     infix_converter = Infix()
#     infix_converter.InfixtoPostfix(infix_expression)
