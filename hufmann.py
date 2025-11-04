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

def print_codes(node, val=''):
    new_val = val + str(node.huff)
    if node.left is None and node.right is None:
        print(f"{node.symbol} -> {new_val}")
        return
    if node.left:
        print_codes(node.left, new_val)
    if node.right:
        print_codes(node.right, new_val)

def huffman_encoding(symbols, frequencies):
    nodes = []
    for i in range(len(symbols)):
        heapq.heappush(nodes, Node(frequencies[i], symbols[i]))

    while len(nodes) > 1:
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)
        left.huff = '0'
        right.huff = '1'
        new_node = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
        heapq.heappush(nodes, new_node)

    print("\nHuffman Codes for each symbol:")
    print_codes(nodes[0])

if __name__ == "__main__":
    n = int(input("Enter number of symbols: "))
    symbols = []
    frequencies = []

    for i in range(n):
        symbol = input(f"Enter symbol {i+1}: ")
        freq = int(input(f"Enter frequency of '{symbol}': "))
        symbols.append(symbol)
        frequencies.append(freq)

    huffman_encoding(symbols, frequencies)
