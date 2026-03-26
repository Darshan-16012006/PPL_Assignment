class Employee:
    def get_data(self):
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))
        self.salary = int(input("Enter salary: "))
        self.address = input("Enter address: ")

class Manager(Employee):
    def display(self):
        print("\nManager Details")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)
        print("Address:", self.address)

# Process information of 2 managers (you can change to 10)
for i in range(2):
    print("\nEnter details of Manager", i+1)
    m = Manager()
    m.get_data()
    m.display()