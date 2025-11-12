
customer_ids = list(map(int, input("Enter Customer Account IDs separated by space: ").split()))


search_id = int(input("Enter the Customer Account ID to search: "))


found = False
for id in customer_ids:
    if id == search_id:
        found = True
        break


if found:
    print(f"Customer Account ID {search_id} found in the list.")
else:
    print(f"Customer Account ID {search_id} not found in the list.")