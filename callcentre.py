from collections import deque

# Queue Implementation
class CallCenterQueue:
    def __init__(self):
        self.queue = deque()

    def addCall(self, customerID, callTime):
        self.queue.append({"CustomerID": customerID, "CallTime": callTime})
        print(f"Call from Customer {customerID} added to the queue.")

    def answerCall(self):
        if self.isQueueEmpty():
            print("No calls to answer.")
        else:
            call = self.queue.popleft()
            print(f"Answered call from Customer {call['CustomerID']} (Call Time: {call['CallTime']} mins).")

    def viewQueue(self):
        if self.isQueueEmpty():
            print("No calls in queue.")
        else:
            print("\nCurrent Call Queue:")
            for i, call in enumerate(self.queue, 1):
                print(f"{i}. CustomerID: {call['CustomerID']}, Call Time: {call['CallTime']} mins")

    def isQueueEmpty(self):
        return len(self.queue) == 0


# Menu-driven main program
call_center = CallCenterQueue()

while True:
    print("\n--- Call Center Menu ---")
    print("1. Add Call")
    print("2. Answer Call")
    print("3. View Queue")
    print("4. Check if Queue is Empty")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        cid = input("Enter Customer ID: ")
        ctime = int(input("Enter Call Time (in minutes): "))
        call_center.addCall(cid, ctime)

    elif ch == 2:
        call_center.answerCall()

    elif ch == 3:
        call_center.viewQueue()

    elif ch == 4:
        print("Queue is empty." if call_center.isQueueEmpty() else "Queue is not empty.")

    elif ch == 5:
        print("Exiting Call Center Simulation.")
        break

    else:
        print("Invalid choice! Please try again.")
