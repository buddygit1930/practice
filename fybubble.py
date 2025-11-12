from array import array

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Main program
n = int(input("Enter number of students: "))
percentages = array('f', [])   # 'f' = float type array

for i in range(n):
    p = float(input(f"Enter percentage of student {i+1}: "))
    percentages.append(p)

bubble_sort(percentages)
print("\nPercentages in Ascending Order:", list(percentages))

# Display top 5 scores
top_five = list(percentages)[-5:][::-1] if n >= 5 else list(percentages)[::-1]
print("Top 5 Scores:", top_five)
