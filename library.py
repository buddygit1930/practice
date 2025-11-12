def average_borrow(library):
    total = sum(library.values())
    n = len(library)
    return total / n if n > 0 else 0

def highest_lowest(library):
    if not library:
        return None
    high = max(library, key=library.get)
    low = min(library, key=library.get)
    return (high, library[high], low, library[low])

def count_zero(library):
    return sum(1 for v in library.values() if v == 0)

def most_frequent(library):
    if not library:
        return None
    max_val = max(library.values())
    return [k for k, v in library.items() if v == max_val]

# --- Main Program ---
library = {}
while True:
    print("\n--- Library Borrowing Menu ---")
    print("1. Add/Update Book Record")
    print("2. Compute Average Borrowings")
    print("3. Find Highest and Lowest Borrowed Book")
    print("4. Count Members with 0 Borrowings")
    print("5. Display Most Frequently Borrowed Book")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        book = input("Enter book name: ")
        count = int(input("Enter number of times borrowed: "))
        library[book] = count
        print("Record added/updated successfully.")

    elif choice == '2':
        avg = average_borrow(library)
        print(f" Average borrowings: {avg:.2f}")

    elif choice == '3':
        result = highest_lowest(library)
        if result:
            high, hv, low, lv = result[0], result[1], result[2], result[3]
            print(f" Highest borrowed: {high} ({hv} times)")
            print(f" Lowest borrowed: {low} ({lv} times)")
        else:
            print(" No records found.")

    elif choice == '4':
        zeros = count_zero(library)
        print(f" Members with 0 borrowings: {zeros}")

    elif choice == '5':
        freq_books = most_frequent(library)
        if freq_books:
            print(" Most frequently borrowed book(s):", ", ".join(freq_books))
        else:
            print(" No records found.")

    elif choice == '6':
        print("Exiting program. ")
        break

    else:
        print(" Invalid choice. Please try again.")
