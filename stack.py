# --- Initialize stacks ---
undo_stack = []
redo_stack = []
document = ""

while True:
    print("\n--- Text Editor Menu ---")
    print("1. Make a Change")
    print("2. Undo Last Change")
    print("3. Redo Last Change")
    print("4. Display Document State")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        change = input("Enter text to add: ")
        undo_stack.append(document)
        document += change
        redo_stack.clear()
        print(" Change applied.")

    elif choice == '2':
        if undo_stack:
            redo_stack.append(document)
            document = undo_stack.pop()
            print(" Undo performed.")
        else:
            print(" No changes to undo.")

    elif choice == '3':
        if redo_stack:
            undo_stack.append(document)
            document = redo_stack.pop()
            print(" Redo performed.")
        else:
            print(" No actions to redo.")

    elif choice == '4':
        print(" Current Document State:", document if document else "[Empty Document]")

    elif choice == '5':
        print(" Exiting program.")
        break

    else:
        print(" Invalid choice! Please try again.")
