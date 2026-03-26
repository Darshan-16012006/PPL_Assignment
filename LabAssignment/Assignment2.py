class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        book = input("Enter book name: ")
        self.books.append(book)

    def display_books(self):
        print("Available Books:", self.books)

    def lend_book(self):
        book = input("Enter book to lend: ")
        if book in self.books:
            self.books.remove(book)
            print("Book issued")
        else:
            print("Book not available")

    def return_book(self):
        book = input("Enter book to return: ")
        self.books.append(book)
        print("Book returned")

lib = Library()

while True:
    print("\n1 Add Book")
    print("2 Display Books")
    print("3 Lend Book")
    print("4 Return Book")
    print("5 Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        lib.add_book()

    elif choice == 2:
        lib.display_books()

    elif choice == 3:
        lib.lend_book()

    elif choice == 4:
        lib.return_book()

    elif choice == 5:
        break