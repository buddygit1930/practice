# Hash table of size 10 (each slot is a list for chaining)
table_size = 10
hash_table = [[] for _ in range(table_size)]

def hash_function(key):
    return key % table_size  # Division method

def insert(key, value):
    index = hash_function(key)
    for pair in hash_table[index]:
        if pair[0] == key:
            pair[1] = value
            print(" Key updated successfully.")
            return
    hash_table[index].append([key, value])
    print("Key inserted successfully.")

def search(key):
    index = hash_function(key)
    for pair in hash_table[index]:
        if pair[0] == key:
            print(f" Found: Key={key}, Value={pair[1]}")
            return
    print(" Key not found.")

def delete(key):
    index = hash_function(key)
    for pair in hash_table[index]:
        if pair[0] == key:
            hash_table[index].remove(pair)
            print(" Key deleted successfully.")
            return
    print(" Key not found.")

def display():
    print("\n--- Hash Table ---")
    for i in range(table_size):
        print(f"{i}: {hash_table[i]}")

# --- Menu-driven program ---
while True:
    print("\n--- Hash Table Menu ---")
    print("1. Insert Key-Value Pair")
    print("2. Search Key")
    print("3. Delete Key")
    print("4. Display Hash Table")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        key = int(input("Enter key (integer): "))
        value = input("Enter value: ")
        insert(key, value)

    elif choice == '2':
        key = int(input("Enter key to search: "))
        search(key)

    elif choice == '3':
        key = int(input("Enter key to delete: "))
        delete(key)

    elif choice == '4':
        display()

    elif choice == '5':
        print(" Exiting program.")
        break

    else:
        print(" Invalid choice! Please try again.")
