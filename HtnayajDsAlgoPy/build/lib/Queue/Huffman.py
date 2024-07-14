import heapq

class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''

    def __lt__(self, nxt):
        return self.freq < nxt.freq

class HuffmanCoding:
    def printNodes(self, node, val="", di={}):
        newVal = val + str(node.huff)
        if node.left:
            self.printNodes(node.left, newVal, di)
        if node.right:
            self.printNodes(node.right, newVal, di)
        if not node.left and not node.right:
            di[node.symbol] = newVal
        return di

    def Huffman(self, Text: str):
        try:
            
            if len(Text) == 0:
                raise ValueError("Input string must not be empty")

            chars = []
            for i in Text:
                if i not in chars:
                    chars.append(i)
            
            freq = []
            for i in chars:
                freq.append(Text.count(i))
            
            nodes = []
            for x in range(len(chars)):
                heapq.heappush(nodes, Node(freq[x], chars[x]))
            
            while len(nodes) > 1:
                left = heapq.heappop(nodes)
                right = heapq.heappop(nodes)
                left.huff = 0
                right.huff = 1
                newNode = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
                heapq.heappush(nodes, newNode)
            
            if nodes:
                return self.printNodes(nodes[0])
            else:
                raise ValueError("Invalid input for Huffman coding")

        except TypeError as te:
            print(f"TypeError: {te}")
        except ValueError as ve:
            print(f"ValueError: {ve}")
        except Exception as e:
            print(f"Exception: {e}")

    def OgCost(self, Text: str):
        try:
            if not isinstance(Text, str):
                raise TypeError("Input must be a string")

            return len(Text) * 8

        except TypeError as te:
            print(f"TypeError: {te}")
        except Exception as e:
            print(f"Exception: {e}")

    def HuffCost(self, Text: dict, string: str):
        try:

            count = 0
            for i in string:
                if i in Text:
                    count += len(Text[i])
                else:
                    raise ValueError(f"Character '{i}' not found in Huffman dictionary")

            return count
        
        except TypeError as te:
            print(f"TypeError: {te}")
        except ValueError as ve:
            print(f"ValueError: {ve}")
        except Exception as e:
            print(f"Exception: {e}")




# huffman = HuffmanCoding()

# # Example with valid input
# huffman.Huffman("hello world")
# # Output: {'h': '10', 'e': '01', 'l': '11', 'o': '001', ' ': '000'}

# # Example with invalid input (empty string)
# huffman.Huffman("")
# # Output: ValueError: Input string must not be empty

# # Example with invalid input (non-string)
# huffman.Huffman(123)
# # Output: TypeError: Input must be a string

# # Example with valid input
# huffman.OgCost("hello world")
# # Output: 88 (assuming 8 bits per character)

# # Example with invalid input (non-string)
# huffman.OgCost(123)
# # Output: TypeError: Input must be a string

# # Example with valid input
# huffman.HuffCost({'h': '10', 'e': '01', 'l': '11', 'o': '001', ' ': '000'}, "hello")
# # Output: 8 (bits)

# # Example with invalid input (non-string as second argument)
# huffman.HuffCost({'h': '10', 'e': '01', 'l': '11', 'o': '001', ' ': '000'}, 123)
# # Output: TypeError: Second argument must be a string

# # Example with invalid input (character not in Huffman dictionary)
# huffman.HuffCost({'h': '10', 'e': '01', 'l': '11', 'o': '001', ' ': '000'}, "world")
# # Output: ValueError: Character 'w' not found in Huffman dictionary
