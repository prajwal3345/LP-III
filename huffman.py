# Write a program to implement Huffman Encoding using a greedy strategy.


import heapq

class node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ""
    
    def __lt__(self, other):
        return self.freq < other.freq
    
def printNodes(node, val=""):
    newval = val + node.huff
    if node.left:
        printNodes(node.left, newval)
    if node.right:
        printNodes(node.right, newval)
    else:
        print(f"{node.symbol} -> {newval}")

chars = ["a", "b", "c", "d", "e", "f"]
freqs = [5, 9, 12, 13, 16, 45]
nodes = []

for i in range(len(chars)):
    heapq.heappush(nodes, node(freqs[i], chars[i]))

while len(nodes) > 1:
    left = heapq.heappop(nodes)
    right = heapq.heappop(nodes)
    left.huff = "0"
    right.huff = "1"
    newnode = node(left.freq + right.freq, left.symbol + right.symbol, left, right)
    heapq.heappush(nodes, newnode)

printNodes(nodes[0])















# heapq is a Python library for working with heaps (priority queues).
# Here, it is used to maintain a min-heap of nodes based on their frequencies
# Defines a node class to represent each node in the Huffman Tree.
# __init__(self, freq, symbol, left=None, right=None): Initializes each node with:
# freq: The frequency of the symbol.
# symbol: The character symbol.
# left and right: Left and right child nodes, set to None by default.
# huff: A string to store the binary code (initialized as an empty string).
# This function __lt__ (less than) overrides the default comparison behavior for nodes.
# It allows heapq to use node frequency as the basis for ordering in the min-heap, comparing nodes by self.freq < other.freq.
# printNodes is a recursive function to print the Huffman codes for each character.
# newval = val + node.huff: Concatenates the current node’s huff code (either "0" or "1") to the accumulated val string.
# if node.left:: If there is a left child, it calls printNodes recursively for the left child, passing the updated newval.
# if node.right:: If there is a right child, it similarly calls printNodes recursively for the right child.
# else:: If the node has no children (i.e., it’s a leaf), it prints the symbol and its Huffman code (newval), 
# representing the final code for that symbol.
# chars: A list of characters.
# freqs: A list of frequencies corresponding to each character.
# nodes: An empty list to hold the nodes that will be added to the min-heap.
# Loops through each character and frequency pair.
# heapq.heappush(nodes, node(freqs[i], chars[i])): Creates a new node for each character and frequency and pushes it into the nodes min-heap.
# while len(nodes) > 1:: Continues until there is only one node left, which will be the root of the Huffman Tree.
# left = heapq.heappop(nodes): Pops the node with the lowest frequency from nodes and assigns it to left.
# right = heapq.heappop(nodes): Pops the next lowest-frequency node and assigns it to right.
# left.huff = "0" and right.huff = "1": Assigns binary codes "0" to the left node and "1" to the right node.
# newnode = node(left.freq + right.freq, left.symbol + right.symbol, left, right): Combines the two nodes into a new node with:
# Frequency equal to the sum of left.freq and right.freq.
# Symbol as a concatenation of left.symbol and right.symbol.
# left and right set as the children of this new node.
# heapq.heappush(nodes, newnode): Pushes the new combined node back into the nodes heap.
# printNodes(nodes[0]): Calls printNodes on the root node of the Huffman Tree (the only node left in nodes) to print the Huffman codes for each character.