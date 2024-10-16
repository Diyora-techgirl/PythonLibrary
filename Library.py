class Library:
    def __init__(self):
        self.books = []

    def show_books(self):
        for book in self.books:
            print(book)

    def get_all_books_as_list(self):
        return [book.get_info_as_list() for book in self.books]

    def get_all_members(self):
        members = []
        try:
            with open("members.txt", 'r') as f:
                lines = f.readlines()
                for line in lines:
                    # Split the line using ", " to extract member info
                    attributes = {kv.split(':')[0].strip(): kv.split(':')[1].strip() for kv in line.split(',') if
                                  ':' in kv}
                    members.append(attributes)  # Append the member's attributes
        except FileNotFoundError:
            print("Members file not found.")
        return members