# Binary Search Implementation in Python
def binary_search(customer_ids, search_id):
    low = 0
    high = len(customer_ids) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if customer_ids[mid] == search_id:
            return True
        elif customer_ids[mid] < search_id:
            low = mid + 1
        else:
            high = mid - 1
    return False

# Main Program
print("=== E-Commerce Customer Account Search System ===")

# Input customer IDs
customer_ids = list(map(int, input("Enter customer account IDs (space-separated): ").split()))

# Binary Search works on a sorted list
customer_ids.sort()
print("Sorted Customer IDs:", customer_ids)

# Input the ID to search
search_id = int(input("Enter the customer ID to search: "))

# Perform binary search
if binary_search(customer_ids, search_id):
    print(f"Customer ID {search_id} found in the system ✅")
else:
    print(f"Customer ID {search_id} not found in the system ❌")
