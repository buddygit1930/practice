# Hash Table implementation using Division Method and Linear Probing

SIZE = 10  # Fixed size of hash table
hash_table = [None] * SIZE

def hash_function(key):
    return key % SIZE  # Division method

def insert(key):
    index = hash_function(key)
    start_index = index
    while hash_table[index] is not None:
        index = (index + 1) % SIZE
        if index == start_index:
            print("Hash table is full!")
            return
    hash_table[index] = key
    print(f"Key {key} inserted at index {index}")

def search(key):
    index = hash_function(key)
    start_index = index
    while hash_table[index] is not None:
        if hash_table[index] == key:
            print(f"Key {key} found at index {index}")
            return
        index = (index + 1) % SIZE
        if index == start_index:
            break
    print(f"Key {key} not found!")

def delete(key):
    index = hash_function(key)
    start_index = index
    while hash_table[index] is not None:
        if hash_table[index] == key:
            hash_table[index] = None
            print(f"Key {key} deleted from index {index}")
            return
        index = (index + 1) % SIZE
        if index == start_index:
            break
    print(f"Key {key} not found!")

def display():
    print("\nHash Table:")
    for i in range(SIZE):
        print(f"Index {i}: {hash_table[i]}")
    print()

# Menu-driven interface
while True:
    print("\nMenu:")
    print("1. Insert a key")
    print("2. Search for a key")
    print("3. Delete a key")
    print("4. Display hash table")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        key = int(input("Enter key to insert: "))
        insert(key)
    elif choice == 2:
        key = int(input("Enter key to search: "))
        search(key)
    elif choice == 3:
        key = int(input("Enter key to delete: "))
        delete(key)
    elif choice == 4:
        display()
    elif choice == 5:
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please try again.")
