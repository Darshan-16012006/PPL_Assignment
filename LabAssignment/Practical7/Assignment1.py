while True:
    print("\n1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Modulus")
    print("6.Exit")

    choice = int(input("Enter choice: "))

    if choice == 6:
        break

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if choice == 1:
        print("Result:", a+b)
    elif choice == 2:
        print("Result:", a-b)
    elif choice == 3:
        print("Result:", a*b)
    elif choice == 4:
        print("Result:", a/b)
    elif choice == 5:
        print("Result:", a%b)