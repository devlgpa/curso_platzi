#crearemos la clase book

class Book:

    #la clase tendra titulo y autor

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    #el libro podra ser prestado y si no es el caso estara disponible

    def borrow(self):
        if self.available:
            self.available = False
            print (f"El libro {self.title} ha sido prestado")
        else:
            print (f"El libro {self.title} no esta disponible")

    #asi como se presta tambien se puede devolver

    def return_book(self):
        self.available = True
        print (f"El libro {self.title} ha sido devuelto")

#aqui crearemos al usuario

class User:

    #el usuario contara con nombre e id y tendra una lista de los libros prestados

    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    #al prestarse un libro este pasara a su lista de prestados

    def borrow_book(self, book):
        if book.available:
            book.borrow()
            self.borrowed_books.append(book)

        #si no se lo puede prestar no saltara este mensaje

        else:
            print (f"El libro {book.title} No esta disponible")

    #podra devolver los libros prestados y seran removidos de su lista

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)

        #si no tiene el libro en su lista saltara este mensaje

        else:
            print (f"El libro {book.title} No esta en la lista de prestados")

#crearemos la clase libreria que contrendra a todos los libros y usuarios

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    #podremos agregar libros

    def add_book(self, book):
        self.books.append(book)
        print(f"El libro {book.title} ha sido agregado")

    #registraremos a nuestro usuario en la lista

    def register_user(self, user):
        self.users.append(user)
        print (f"El usuario {user.name} ha sido registrado")

    #nos mostrara la lista de libros disponibles

    def show_available_books(self):
        print ("Libros disponibles:")
        for book in self.books:
            if book.available:
                print(f"{book.title} por {book.author}")

#crearemos los libros

book1 = Book("La niebla", "Stepehn King")
book2 = Book("El principito", "Antoine de Saint-Exupéry")
book3 = Book("1984", "George Orwell")

#Crear usuario

user1 = User("Chalo", "001")

#Crear la biblioteca
library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.register_user(user1)

#Mostrar libros
library.show_available_books()

#Realizar prestamos
user1.borrow_book(book1)

#Mostrar libros
library.show_available_books()

#Devolver libro
user1.return_book(book1)

#Mostrar libros
library.show_available_books()
