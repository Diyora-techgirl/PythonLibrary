from Tools import Tools
class Member:
    def __init__(self, name, age, login, password):
        self.name = name
        self.age = age
        self.login = login
        self.password = password
        self.card_number = Tools.id_generator()

    def __str__(self):
        return f"Name: {self.name}, ID: {self.card_number}, Age: {self.age}, Login: {self.login}, Password: {self.password}/n"

    def show_info(self):
        print(self)

    def borrow_book(self, book_name, books):
        book = next((b for b in books if b.name.lower() == book_name.lower()), None)  # Find the book by name
        if book is None:
            print(f"Sorry, the book '{book_name}' does not exist.")
            return

        if not book.borrowed:
            book.borrowed = True  # Set the book as borrowed
            print(f"{self.name} borrowed the book '{book.name}'.")
        else:
            print(f"Sorry, the book '{book.name}' is already borrowed.")

    def return_book(self, book_name, books):
        # Find the book by name
        book = next((b for b in books if b.name.lower() == book_name.lower()), None)
        if book:
            if book.borrowed:
                book.borrowed = False  # Set the book as available
                print(f"{self.name} returned the book '{book.name}'.")
            else:
                print(f"The book '{book.name}' was not borrowed.")
        else:
            print(f"The book '{book_name}' does not exist in the library.")

    def view_books(self, books):
        print("Available books in the library:")
        available_books = [book for book in books if not book.borrowed]
        if available_books:
            for idx, book in enumerate(available_books, 1):
                print(f"{idx}. {book}")
        else:
            print("No available books.")

    def show_functions(self, books):
        while True:
            print("\n--- Member Menu ---")
            print("1. View available books")
            print("2. Borrow a book")
            print("3. Return a book")
            print("0. Log out")
            choice = int(input("Select an option: "))
            if choice == 1:
                self.view_books(books)
            elif choice == 2:
                book_to_borrow = input("Enter the name of the book to borrow: ")
                self.borrow_book(book_to_borrow, books)
            elif choice == 3:
                book_to_return = input("Enter the name of the book to return: ")
                self.return_book(book_to_return, books)  # Pass the books list
            elif choice == 0:
                print("Logging out...")
                break
            else:
                print("Invalid choice, please try again.")
