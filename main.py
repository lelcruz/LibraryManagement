# Notes:
# The library is not inheriting from books
# This type of class is more of a composition method in this class which a library has books

class book:
    def __init__(self):
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
        print("Books in the library:")
        for book in self.library_books:
            print(book)

    def checkout_book(self):
        checkout = input("Please enter the book you would like to checkout: ")
        if not self.library_books:
            print("Library is currently empty")
        for book in self.library_books:
            if book.title == checkout:
                if book.status == "unavailable":
                    print("The book you are trying to checkout is currently unavailable.")
                else:
                    print("You have now checked out:", book.title)
                    book.status = "unavailable"
            elif book.title != checkout:
                print("Sorry book is not in our library selection")


    def return_book(self):
        return_book = input("Please enter the book you are returning: ")
        for book in self.library_books:
            if book.title == return_book:
                if book.status == "available":
                    print("The book you are trying to return is currently available.")
                else:
                    print("You have now returned:", book.title)
                    book.status = "available"
            elif book.title != return_book:
                print("Sorry book is not in our library selection")

def main():
    cozy_reads = library()
    while True:

        print("\nHi, welcome to Cozy Reads")
        print("Choose from the menu below:")
        print("1: Add book to library")
        print("2: View libray selection")
        print("3: Checkout book from library")
        print("4: Return book to library")
        print("5: Exit library")
        option = int(input("Enter your choice: "))

        if option == 1:
            new_book = book()
            cozy_reads.adding_book(new_book)
        elif option == 2:
            cozy_reads.viewing_library()
        elif option == 3:
            cozy_reads.checkout_book()
        elif option == 4:
            cozy_reads.return_book()
        elif option == 5:
            break


if __name__ == "__main__":
    main()
