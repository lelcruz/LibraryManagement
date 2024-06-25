# Notes:
# The library is not inheriting from books
# This type of class is more of a composition class which a library has books

class book:
    def __init__(self, title=None, author=None, status=None):
        self.title = input("Title: ")
        self.author = input("Author:")
        self.status = input("Status: ")

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Status: {self.status}"


class library:
    def __init__(self):
        self.library_books = []

    def adding_book(self, book):
        self.library_books.append(book)

    def viewing_library(self):
        if self.library_books:
            print("Books in the library: ")
            for book in self.library_books:
                print(book, "\n")



def main():
    temp = library()
    while True:
        print("Hi, welcome to Cozy Reads")
        print("Choose from the menu below:")
        print("1: Add book to library")
        print("2: View libray")
        option = int(input("Enter your choice: "))

        if option == 1:
            book_added = book()
            temp.adding_book(book_added)
        elif option == 2:
            temp.viewing_library()


if __name__ == "__main__":
    main()
