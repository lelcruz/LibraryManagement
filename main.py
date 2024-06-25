# Notes:
# passing the copy not the actual thing
# What's inside the function doesn't exist to outside the function

class book:
    def __init__(self, title, author, status):
        self.title = title
        self.author = author
        self.status = status

    def book_status(self):
        print("Title: ", self.title)
        print("Author: ", self.author)
        print("Status: ", self.status)

class library(book):
    def __init__(self, title, author, status):
        super().__init__(title,author, status)
        self.library_books = []




def main():
    print("Hi, welcome to Cozy Reads")
    print("Choose from the menu bellow what you would like to do.")
    print("1: Add book to library")
    print("2: View libray")
    option = input("Enter your choice: ")




if __name__ == "__main__":
    main()