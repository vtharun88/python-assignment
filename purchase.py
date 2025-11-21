# Program to read purchase file and calculate bill details

file_name = input("Enter purchase file name: ")

# Variables to store results
items_purchased = 0
free_items = 0
amount_to_pay = 0
discount = 0

with open(file_name, "r") as f:
    for line in f:
        line = line.strip()

        # Skip empty lines
        if line == "":
            continue

        # Check for free items
        if line.endswith("Free"):
            free_items += 1

        # Check for discount line
        elif line.startswith("Discount"):
            parts = line.split()
            discount = int(parts[1])

        # Otherwise, it's a purchased item with price
        else:
            parts = line.split()
            price = int(parts[-1])   # last part is price
            items_purchased += 1
            amount_to_pay += price

# Calculate final amount
final_amount = amount_to_pay - discount

# ---- OUTPUT ----
print("No of items purchased:", items_purchased)
print("No of free items:", free_items)
print("Amount to pay:", amount_to_pay)
print("Discount given:", discount)
print("Final amount paid:", final_amount)
