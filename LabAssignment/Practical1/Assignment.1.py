name = input("Enter employee name: ")
emp_id = input("Enter employee ID: ")
department = input("Enter department: ")
basic = float(input("Enter basic salary: "))

DA = 0.92 * basic
HRA = 0.58 * basic
TA = 0.30 * basic
LIC = 500

gross_salary = basic + DA + HRA + TA
net_salary = gross_salary - LIC

print("\nEmployee Details")
print("Name:", name)
print("ID:", emp_id)
print("Department:", department)
print("Basic Salary:", basic)
print("Gross Salary:", gross_salary)
print("Net Salary:", net_salary)