from Tools import Tools
from Book import Book
from Member import Member

class Librarian:
    def __init__(self, name, age, login, password):
        self.__name = name
        self.__age = age
        self.__login = login
        self.__password = password
        self.__member_list = []
        self.__book_list = []

    def add_member(self, member_info):
        new_member = Member(member_info['Name'], member_info['Age'], member_info['Login'], member_info['Password'])
        self.__member_list.append(new_member)

    def add_book(self, book):
        self.__book_list.append(book)

    def show_members(self):
        print("Members in the library:")
        for member in self.__member_list:
            print(member)

    def show_books(self):
        print("Books in the library:")
        for book in self.__book_list:
            print(book)

    def get_login(self):
        return self.__login
