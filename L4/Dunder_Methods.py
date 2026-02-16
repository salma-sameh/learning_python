#Dunder = Double Under __
class Book:
    def __init__(self, title, author, pages): # constructor
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self): #Controls what prints when you print an object.
        return f"'{self.title}' by {self.author}"

    def __repr__(self):#Shows technical representation of the object.
        return f"Book('{self.title}', '{self.author}', {self.pages})"

    def __len__(self): # return the object length
        return self.pages
    def __add__(self, other): #allow you to add 2 objects together.
        return self.pages + other.pages

    def __del__(self):#Runs automatically when object is deleted from memory.
        print(f"Book '{self.title}' is being destroyed")

book1 = Book("Python 101", "John Doe", 300)
book2 = Book("Data Science", "Jane Smith", 450)

print(book1)        # Output: 'Python 101' by John Doe
print(repr(book1))  # Output: Book('Python 101', 'John Doe', 300)
print(len(book1))   # Output: 300
print(book1 + book2) # Output: 750

del book1  # Output: Book 'Python 101' is being destroyed
