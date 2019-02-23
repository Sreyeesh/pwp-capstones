

class User:
    def __init__(self, name, email):
        self.name = name      
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, email):
        self.email = email
        return "Thanks for updating your email! Your new email is: " + self.email
        
    print("E-mail address updated.")


    def __repr__(self):
        return f"User: {self.name} , email: {self.email} , books read: {self.books}"

    def __eq__(self, user):
        return self.name == user.name and self.email == user.email

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        temp_rating = [rating for rating in self.books.values() if rating is not None]
        return sum(temp_rating) / len(temp_rating)

class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        return "This book's ISBN has been updated. It is now: " + str(new_isbn)


    def add_rating(self, rating):
            if 0 <= rating <= 4:
                self.ratings.append(rating)
            else:
                print("Invalid Rating")

    

    def get_average_rating(self):
        temp_rating = [rating for rating in self.ratings if rating is not None]
        return sum(temp_rating) / len(temp_rating)

    def __eq__(self, book):
        return self.title == book.title and self.isbn == book.isbn

    def __hash__(self):
        return hash((self.title, self.isbn))

    def __repr__(self):
        return f"{self.title}"

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author
    
    def __repr__(self):
        return f"{self.title} by {self.author}"

class NonFiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return f"{self.title}, a {self.level} manual on {self.subject}"

class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {} # dict containing book names and the number of people that have read the book. 

    def create_book(self, title, isbn):
        book = Book(title, isbn)
        return book

    def create_novel(self, title, author, isbn):
        novel = Fiction(title, author, isbn)
        return novel

    def create_non_fiction(self, title, subject, level, isbn):
        non_fiction = NonFiction(title, subject, level, isbn)
        return non_fiction
    
    def add_book_to_user(self, book, email, rating=None):
        if email in self.users:
            self.users[email].read_book(book, rating)
            if rating:
                book.add_rating(rating)
            
            if book not in self.books:
                self.books[book] = 1
            else:
                updated_book = {book : self.books[book] + 1}
                self.books.update(updated_book)
        
        else:
            print(f"No user with email {email}")

    def add_user(self, name, email, user_books=None):
        user = User(name, email)
        self.users[user.email] = user
        if user_books:
            for book in user_books:
                self.add_book_to_user(book, email)

    def print_catalog(self):
        for book in self.books.keys():
            print(book)

    def print_users(self):
        for user in self.users.keys():
            print(self.users[user].name)

    def most_read_book(self):
        return max(self.books.keys(), key=(lambda key : self.books[key]))

    def highest_rated_book(self):
        max_rating = 0
        highest_rated_book = None
        for book in self.books.keys():
            if book.get_average_rating() > max_rating:
                highest_rated_book = book
        return highest_rated_book

    def most_positive_user(self):
        max_rating = 0
        most_positive_user = None
        for user in self.users.keys():
            if self.users[user].get_average_rating() > max_rating:
                most_positive_user = user
        return self.users[most_positive_user].name
        












        
            


    

    


            




    


    

    



    

    