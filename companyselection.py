def selection_sort(salaries):
    n = len(salaries)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if salaries[j] < salaries[min_idx]:
                min_idx = j
        salaries[i], salaries[min_idx] = salaries[min_idx], salaries[i]

# Main program
salaries = list(map(float, input("Enter employee salaries: ").split()))

selection_sort(salaries)
print("\nSalaries in Ascending Order:", salaries)

# Display top 5 highest salaries
top_five = salaries[-5:][::-1] if len(salaries) >= 5 else salaries[::-1]
print("Top 5 Highest Salaries:", top_five)
