def bubble_sort(salaries):
    n = len(salaries)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if salaries[j] > salaries[j + 1]:
                salaries[j], salaries[j + 1] = salaries[j + 1], salaries[j]

# Main program
salaries = list(map(float, input("Enter employee salaries: ").split()))

bubble_sort(salaries)
print("\nSalaries in Ascending Order:", salaries)

# Display top 5 highest salaries
top_five = salaries[-5:][::-1] if len(salaries) >= 5 else salaries[::-1]
print("Top 5 Highest Salaries:", top_five)
