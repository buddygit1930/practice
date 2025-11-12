from array import array

# Function for Linear Search
def linear_search(roll_numbers, search_roll):
    for roll in roll_numbers:
        if roll == search_roll:
            return True
    return False

# Main Program
print("=== Student Attendance Search System (Using Array) ===")

# Input roll numbers of students who attended the training program
roll_numbers = array('i', map(int, input("Enter roll numbers of students (space-separated): ").split()))

# Input roll number to search
search_roll = int(input("Enter roll number to search: "))

# Perform linear search
if linear_search(roll_numbers, search_roll):
    print(f"Student with Roll Number {search_roll} attended the training program ")
else:
    print(f"Student with Roll Number {search_roll} did NOT attend the training program ")

