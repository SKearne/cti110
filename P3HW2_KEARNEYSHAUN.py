# Shaun Kearney
# June 29, 2025
# P3HW2

# Pseudocode:
# 1. Get the employee's name from the user.
# 2. Get the number of hours worked from the user.
# 3. Get the employee's pay rate from the user.
# 4. Check if the employee has worked overtime (more than 40 hours).
# 5. If overtime is worked, calculate the amount owed for overtime hours (overtime pay = (hours worked - 40) * (pay rate * 1.5)).
# 6. Calculate the amount owed for regular hours (regular pay = hours worked * pay rate).
# 7. Calculate the gross pay (gross pay = regular pay + overtime pay).
# 8. Display employee name, pay rate, number of hours worked, overtime hours, overtime pay, pay for regular hours, and gross pay.

# Get employee's name:
employee_name = input("Enter employee's name: ")

# Get number of hours worked:
hours_worked = float(input("Enter number of hours worked: "))

# Get employee's pay rate:
pay_rate = float(input("Enter employee's pay rate: "))
print("-----------------------------------")
# Check for overtime:
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    regular_pay = 40 * pay_rate
else:
    overtime_hours = 0
    overtime_pay = 0
    regular_pay = hours_worked * pay_rate

# Calculate gross pay:
gross_pay = regular_pay + overtime_pay

# Display the results:
print("Employee Name:", employee_name)
print("Pay Rate:", pay_rate)
print("Number of Hours Worked:", hours_worked)
print("Overtime Hours:", overtime_hours)
print("Overtime Pay:", overtime_pay)
print("Pay for Regular Hours:", regular_pay)
print("Gross Pay:", gross_pay)

