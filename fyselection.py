from array import array

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Main program
n = int(input("Enter number of students: "))
percentages = array('f', [])   # 'f' = float type array

for i in range(n):
    p = float(input(f"Enter percentage of student {i+1}: "))
    percentages.append(p)

selection_sort(percentages)
print("\nPercentages in Ascending Order:", list(percentages))

# Display top 5 scores
top_five = list(percentages)[-5:][::-1] if n >= 5 else list(percentages)[::-1]
print("Top 5 Scores:", top_five)
