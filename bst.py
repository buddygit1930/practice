# Binary Search Tree Implementation (Insertion, Deletion, Search, Display)

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Insert a new key
def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    return root

# Search a key
def search(root, key):
    if root is None:
        return False
    if root.key == key:
        return True
    elif key < root.key:
        return search(root.left, key)
    else:
        return search(root.right, key)

# Find minimum node
def find_min(root):
    while root.left:
        root = root.left
    return root

# Delete a key
def delete(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        # Node found
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        temp = find_min(root.right)
        root.key = temp.key
        root.right = delete(root.right, temp.key)
    return root

# Display (Inorder Traversal)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

# Menu-driven program
root = None
while True:
    print("\nMenu:")
    print("1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display (Inorder)")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        key = int(input("Enter value to insert: "))
        root = insert(root, key)
        print("Node inserted.")
    elif choice == 2:
        key = int(input("Enter value to search: "))
        print("Found!" if search(root, key) else "Not found!")
    elif choice == 3:
        key = int(input("Enter value to delete: "))
        root = delete(root, key)
        print("Node deleted (if it existed).")
    elif choice == 4:
        print("Inorder Traversal:", end=" ")
        inorder(root)
        print()
    elif choice == 5:
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.")
