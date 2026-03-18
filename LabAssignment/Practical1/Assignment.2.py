name = input("Enter vendor name: ")
year = input("Enter year of association: ")
contact = input("Enter contact number: ")
email = input("Enter email ID: ")

total = 0

for i in range(1, 13):
    purchase = float(input(f"Enter purchase for month {i}: "))
    total += purchase

print("\nVendor Details")
print("Name:", name)
print("Year:", year)
print("Contact:", contact)
print("Email:", email)
print("Annual Purchase:", total)