employees = []   

while True:
    name = input("Enter employee name (or type 'stop' to finish): ")

    if name.lower() == "stop":
        break

    try:
        basic = float(input(f"Enter basic salary of {name}: "))
    except ValueError:
        print("Invalid salary! Please enter a numeric value.")
        continue

    hra = 0.20 * basic
    da = 0.10 * basic
    total_salary = basic + hra + da

    employees.append((name, total_salary))

print("\n----- Employee Salary Details -----")
for emp_name, total in employees:
    print(f"Employee: {emp_name},   Total Salary: ₹{total:.2f}")
    