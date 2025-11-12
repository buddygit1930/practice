from collections import deque

# Job Queue Implementation
class JobQueue:
    def __init__(self):
        self.queue = deque()

    def addJob(self, jobName):
        self.queue.append(jobName)
        print(f"Job '{jobName}' added to the queue.")

    def deleteJob(self):
        if self.isEmpty():
            print("No jobs to process. Queue is empty.")
        else:
            job = self.queue.popleft()
            print(f"Job '{job}' has been processed and removed from the queue.")

    def viewJobs(self):
        if self.isEmpty():
            print("No jobs in the queue.")
        else:
            print("\nCurrent Jobs in Queue:")
            for i, job in enumerate(self.queue, 1):
                print(f"{i}. {job}")

    def isEmpty(self):
        return len(self.queue) == 0


# Main Program (Menu-Driven)
job_queue = JobQueue()

while True:
    print("\n--- Job Queue Menu ---")
    print("1. Add Job")
    print("2. Delete (Process) Job")
    print("3. View Jobs")
    print("4. Check if Queue is Empty")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        name = input("Enter Job Name: ")
        job_queue.addJob(name)
    elif ch == 2:
        job_queue.deleteJob()
    elif ch == 3:
        job_queue.viewJobs()
    elif ch == 4:
        print("Queue is empty." if job_queue.isEmpty() else "Queue is not empty.")
    elif ch == 5:
        print("Exiting Job Queue Simulation.")
        break
    else:
        print("Invalid choice! Please try again.")
