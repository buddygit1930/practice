from array import array

# Function for Binary Search
def binary_search(roll_numbers, search_roll):
    low = 0
    high = len(roll_numbers) - 1

    while low <= high:
        mid = (low + high) // 2

        if roll_numbers[mid] == search_roll:
            return True
        elif roll_numbers[mid] < search_roll:
            low = mid + 1
        else:
            high = mid - 1
    return False

# Main Program
print("=== Student Attendance Search System (Using Array & Binary Search) ===")

# Input roll numbers of students who attended the training program
roll_numbers = array('i', map(int, input("Enter roll numbers of students (space-separated): ").split()))

# Sort the array (Binary Search requires sorted data)
roll_numbers = array('i', sorted(roll_numbers))
print("Sorted Roll Numbers:", list(roll_numbers))

# Input roll number to search
search_roll = int(input("Enter roll number to search: "))

# Perform binary search
if binary_search(roll_numbers, search_roll):
    print(f" Student with Roll Number {search_roll} attended the training program.")
else:
    print(f"Student with Roll Number {search_roll} did NOT attend the training program.")
