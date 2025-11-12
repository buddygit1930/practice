from collections import deque

# Initialize queue
event_queue = deque()

while True:
    print("\n--- Real-Time Event Processing Menu ---")
    print("1. Add an Event")
    print("2. Process Next Event")
    print("3. Display Pending Events")
    print("4. Cancel an Event")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        event = input("Enter event name: ")
        event_queue.append(event)
        print(f"Event '{event}' added to queue.")

    elif choice == '2':
        if event_queue:
            current = event_queue.popleft()
            print(f" Processing event: {current}")
        else:
            print(" No events to process.")

    elif choice == '3':
        if event_queue:
            print(" Pending Events:", list(event_queue))
        else:
            print(" No pending events.")

    elif choice == '4':
        if event_queue:
            event = input("Enter event name to cancel: ")
            if event in event_queue:
                event_queue.remove(event)
                print(f" Event '{event}' canceled.")
            else:
                print(" Event not found in queue.")
        else:
            print(" No events to cancel.")

    elif choice == '5':
        print(" Exiting program.")
        break

    else:
        print(" Invalid choice! Please try again.")
