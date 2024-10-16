from enum import member

from Book import Book
from Member import Member
from Librarian import Librarian
from InputForm import show_librarian_menu, input_form_member, input_form_librarian
from Tools import Tools


def main():
    books = [
        Book("The Great Gatsby", "F. Scott Fitzgerald", 10.99),
        Book("1984", "George Orwell", 8.99),
        Book("To Kill a Mockingbird", "Harper Lee", 7.99),
        Book("Pride and Prejudice", "Jane Austen", 6.99),
        Book("The Catcher in the Rye", "J.D. Salinger", 9.99),
        Book("The Hobbit", "J.R.R. Tolkien", 12.99),
        Book("Moby-Dick", "Herman Melville", 11.50),
        Book("War and Peace", "Leo Tolstoy", 14.99),
        Book("Crime and Punishment", "Fyodor Dostoevsky", 9.49),
        Book("The Picture of Dorian Gray", "Oscar Wilde", 8.49),
    ]
    librarians = []  # List to store librarian instances
    members_file="members.txt"

    def get_all_members(members_file):
        """Read and return all members from the members file."""
        members = []
        try:
            with open(members_file, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    # Split the line using ", " to extract member info
                    attributes = {kv.split(':')[0].strip(): kv.split(':')[1].strip() for kv in line.split(',') if
                                  ':' in kv}
                    members.append(attributes)  # Append the member's attributes
        except FileNotFoundError:
            print("Members file not found.")
        except Exception as e:
            print(f"An error occurred: {e}")  # Catch other possible exceptions
        return members
    while True:
        role = input("Are you a librarian or member? ").strip().lower()
        if role == "librarian":
            registered = input("Are you registered before? (yes/no) ").strip().lower()
            if registered == "yes":
                login = input("Enter your login: ")
                password = input("Enter your password: ")
                valid, librarian = Tools.login_system(login, password, "librarian.txt")
                if valid:
                    print("Login successful!")
                    print(f"Welcome, Librarian: {librarian.get('Login')}")

                    while True:
                        # Show the librarian menu and get choice
                        show_librarian_menu(librarian)  # Pass the librarian object as an argument
                        librarian_choice = int(input("Select an option: "))

                        if librarian_choice == 1:
                            # Logic to add a new member
                            name = input("Enter name of member: ")
                            age = input("Enter age: ")
                            login = input("Enter your login: ")
                            password = input("Enter your password: ")

                            # Create a new member instance
                            new_member = Member(name, age, login, password)
                            member_info = f"Name: {new_member.name}, ID: {Tools.id_generator()}, Age: {new_member.age}, Login: {new_member.login}, Password: {new_member.password}"

                            # Store new member (you need to implement the register_user method)
                            Tools.register_user(member_info, "members.txt")
                            print("Member added successfully!")

                        elif librarian_choice == 2:
                            book_name = input("Enter the book name: ")
                            book_author = input("Enter the book author: ")
                            book_price = float(input("Enter the book price: "))
                            new_book = Book(book_name, book_author, book_price)
                            books.append(new_book)
                            print(f"Book '{book_name}' added successfully!")

                        elif librarian_choice == 3:
                            print("Members in the library:")
                            members = get_all_members(members_file)  # Get all members
                            if members:
                                for m in members:
                                    print(m)  # Print each member's details
                            else:
                                print("No members found.")

                        elif librarian_choice == 4:
                            print("Books in the library:")
                            for book in books:
                                print(book)  # Display all books

                        elif librarian_choice == 0:
                            print("Logging out...")
                            break  # Exit the librarian loop

                        else:
                            print("Invalid choice, please try again.")
                else:
                    print("Invalid login or password.")
            else:
                new_librarian = input_form_librarian()
                librarian_info = f"Name: {new_librarian.get_name()}, ID: {Tools.id_generator()}, Age: {new_librarian.get_age()}, Login: {new_librarian.get_login()}, Password: {new_librarian.get_password()}"
                Tools.register_user(librarian_info, "librarian.txt")
                print("Registration successful!")

        elif role == "member":
            registered = input("Are you registered before? (yes/no) ").strip().lower()
            if registered == "yes":
                login = input("Enter your login: ")
                password = input("Enter your password: ")
                valid, member = Tools.login_system(login, password, "members.txt")
                if valid:
                    print("Welcome back!")
                    member_instance = Member(member.get('Name'), member.get('Age'), member.get('Login'),
                                             member.get('Password'))
                    member_instance.show_functions(books)  # Call the show_functions method with the list of books
                else:
                    print("Invalid login or password.")
            else:
                new_member = input_form_member()
                member_info = f"Name: {new_member.get_name()}, ID: {Tools.id_generator()}, Age: {new_member.get_age()}, Login: {new_member.get_login()}, Password: {new_member.get_password()}"
                Tools.register_user(member_info, "members.txt")
                print("Registration successful!")

        else:
            print("Invalid role. Please choose 'librarian' or 'member'.")


if __name__ == "__main__":
    main()
