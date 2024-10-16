import string
import random


class Tools:
    @staticmethod
    def login_system(login, password, text):
        try:
            with open(text, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    attributes = {kv.split(':')[0].strip(): kv.split(':')[1].strip() for kv in line.split(',') if ':' in kv}
                    if attributes.get("Login") == login and attributes.get("Password") == password:
                        return True, attributes  # Return the found attributes (user/librarian info)

        except FileNotFoundError:
            print("File not found.")
        return False, None  # Return None if not found

    @staticmethod
    def register_user(info, text):
        try:
            with open(text, 'a') as f:
                f.write(str(info) + '\n')  # Append new info to the file with a newline
        except FileNotFoundError:
            print("The file was not found.")

    @staticmethod
    def id_generator(length=5):
        characters = string.digits
        return ''.join(random.choice(characters) for _ in range(length))

