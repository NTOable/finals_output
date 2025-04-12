class Author :
    def __init__(self, initial : str, name : str, email : str) :
        self.initial = initial
        self.name = name
        self.email = email
    #dunder method to print authors
    def __str__(self) :
        return (f"Author Details: \n"
                f"Name: {self.name} \n"
                f"Initials: {self.initial} \n"
                f"Email Address: {self.email} \n")

class Book :
    def __init__(self, code : str, title : str, type : str, rating : str) :
        self.code = code
        self.title = title
        self.type = self.Genre(type,rating)
        self.authors = []
#Book uses composition to link with Author instead of inheritance
    class Genre :
        def __init__(self, genre : str, rating : str) :
            self.genre = genre
            self.rating = rating
    #method to use author instances with books
    def add_author(self, author) :
        self.authors.append(author)
    #dunder method to print books
    def __str__(self) :
        author_initial = ','.join(author.initial for author in self.authors)
        author_name = ','.join(author.name for author in self.authors)
        return (f"Publication Details: \n"
                f"Book Title: {self.title} \n"
                f"Author: {author_initial}, {author_name} \n"
                f"Library Code: {self.code} \n"
                f"Genre: {self.type.genre} \n"
                f"Maturity: {self.type.rating} \n")

class Reader :
    def __init__(self, name : str, age : int) :
        self.name = name
        self.age = age
        self.books = []
    #method to use book instances with readers
    def add_book(self, book) :
        self.books.append(book)
    #dunder method to print readers
    def __str__(self) :
        book_code = ','.join(book.code for book in self.books)
        book_title = ','.join(book.title for book in self.books)
        return (f"Borrower's Details: \n"
                f"Name: {self.name} \n"
                f"Age: {self.age} \n"
                f"Book Title: {book_title} \n"
                f"Code: {book_code} \n")

#readers can have books but books can be without a reader
#instances (author)
author1 = Author("K.S.V", "Kaye Sia Vernon","versia@hotmail.com")
author2 = Author("G.J.L", "Gauss Jean-Luc", "jlgauss@yahoo.com")
#instances (book w/ nested genre, author list)
book1 = Book("PS9223", "Carl Jung: Map of the Soul", "Psychology", "Young Adult+")
book1.add_author(author1)
book2 = Book("ROM4920", "The Only One Who Did", "Romance", "Adult+")
book2.add_author(author2)
#instances (reader w/ book list)
reader1 = Reader("Leroy Sadia", 24)
reader1.add_book(book1)
reader2 = Reader("Heather Maaba", 28)
#print
print(author1)
print(author2)
print(book1)
print(book2)
print(reader1)
print(reader2)