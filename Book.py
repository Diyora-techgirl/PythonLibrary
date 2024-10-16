class Book:
    def __init__(self, name, author, price):
        self.name = name
        self.author = author
        self.price = price
        self.borrowed = False

    def __str__(self):
        return f"Book Name: {self.name}, Author: {self.author}, Price: {self.price}, isAvailable:{self.borrowed}"
