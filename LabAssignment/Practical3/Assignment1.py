students = {}

while True:
    print("\n1.Add Student")
    print("2.View Students")
    print("3.Update Student")
    print("4.Delete Student")
    print("5.Search Student")
    print("6.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        sid = input("Enter ID: ")
        name = input("Enter Name: ")
        students[sid] = name

    elif choice == 2:
        print("Student List:", students)

    elif choice == 3:
        sid = input("Enter ID to update: ")
        if sid in students:
            students[sid] = input("Enter new name: ")

    elif choice == 4:
        sid = input("Enter ID to delete: ")
        students.pop(sid, None)

    elif choice == 5:
        sid = input("Enter ID to search: ")
        print("Student:", students.get(sid,"Not Found"))

    elif choice == 6:
        break