def show_librarian_menu(librarian):
    print("\n--- Librarian Menu ---")
    print("1. Add Member")
    print("2. Add Book")
    print("3. Show Members")
    print("4. Show Books")
    print("0. Logout")

def input_form_member():
    name = input("Enter member name: ")
    age = input("Enter member age: ")
    login = input("Enter member login: ")
    password = input("Enter member password: ")
    return {'Name': name, 'Age': age, 'Login': login, 'Password': password}

def input_form_librarian():
    name = input("Enter librarian name: ")
    age = input("Enter librarian age: ")
    login = input("Enter librarian login: ")
    password = input("Enter librarian password: ")
    return {'Name': name, 'Age': age, 'Login': login, 'Password': password}
