def avg(marks):
    valid = [m for m in marks if m != -1]
    return sum(valid)/len(valid) if valid else 0

def high_low(marks):
    valid = [m for m in marks if m != -1]
    return max(valid), min(valid) if valid else (None, None)

def absent_count(marks):
    return marks.count(-1)

def highest_freq(marks):
    valid = [m for m in marks if m != -1]
    return max(valid, key=valid.count) if valid else None

marks = list(map(int, input("Enter marks of students (-1 for absent): ").split()))

while True:
    print("\n1.Average  2.Highest/Lowest  3.Absent Count  4.Highest Frequency  5.Exit")
    ch = int(input("Enter choice: "))
    
    if ch == 1:
        print("Average Score:", avg(marks))
    elif ch == 2:
        h, l = high_low(marks)
        print("Highest:", h, "Lowest:", l)
    elif ch == 3:
        print("Absent Students:", absent_count(marks))
    elif ch == 4:
        print("Mark with Highest Frequency:", highest_freq(marks))
    elif ch == 5:
        break
    else:
        print("Invalid choice!")
