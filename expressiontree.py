class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Function to check if a character is an operator
def isOperator(c):
    return c in ['+', '-', '*', '/', '^']

# Function to construct expression tree from prefix expression
def constructTree(prefix):
    stack = []
    # Traverse from right to left (prefix rule)
    for symbol in reversed(prefix):
        node = Node(symbol)
        if isOperator(symbol):
            node.left = stack.pop()
            node.right = stack.pop()
        stack.append(node)
    return stack[-1]

# Non-recursive postorder traversal
def postorder_non_recursive(root):
    if not root:
        return []
    stack1, stack2 = [root], []
    while stack1:
        node = stack1.pop()
        stack2.append(node)
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
    return [node.value for node in reversed(stack2)]

# Function to delete the tree
def deleteTree(root):
    if root:
        root.left = None
        root.right = None
    return None

# Main Program
prefix = input("Enter prefix expression (e.g. +--a*bc/def): ")

root = constructTree(prefix)
print("\nPostorder Traversal (Non-Recursive):")
print(" ".join(postorder_non_recursive(root)))

root = deleteTree(root)
print("\nTree deleted successfully.")
