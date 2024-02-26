class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_available = True

    def check_out(self):
        self.is_available = False

    def check_in(self):
        self.is_available = True

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.publication_year}, Available: {self.is_available}"

# Create instances of the Book class
book1 = Book("The Catcher in the Rye", "J.D. Salinger", 1951)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)

# Check out and check in a book
book1.check_out()
book1.check_in()

# Print information about both books
print("Book 1 Information:")
print(book1)

print("\nBook 2 Information:")
print(book2)
