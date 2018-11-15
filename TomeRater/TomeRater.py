#For the "Get Creative!" section, the sophisticated analysis methods were chosen

class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}
       

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("Your email address has been updated to " + address + ".")

    def read_book(self, book, rating = None):
        self.books[book] = rating

    def get_average_rating(self):
        sum = 0
        for rating in self.books.values():
            if rating is None:
                sum += 0
            else:
                sum += rating
        return sum/len(self.books)

    def __repr__(self):
        return "User " + self.name + ", email: " + self.email + ", books read: " + str(len(self.books))

    def __eq__(self, other_user):
        return self.name == other_user.name and self.email == other_user.email

class Book(object):
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
        print("The ISBN number of the book " + self.title + " has been updated to " + str(self.isbn) + ".")

    def add_rating(self, rating):
        if rating:
            if rating >= 0 and rating <= 4:
                self.ratings.append(rating)

            else:
                print("Invalid Rating")

    def get_average_rating(self):
        sum = 0
        for rating in self.ratings:
            sum += rating
        return sum

    def __eq__(self, other_book):
        return self.title == other_book.title and self.isbn == other_book.isbn

    def __hash__(self):
        return hash((self.title, self.isbn))

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author}".format(title = self.title, author = self.author)

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title = self.title, level = self.level, subject = self.subject)

class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        book = Book(title, isbn)
        return book

    def create_novel(self, title, author, isbn):
        fiction = Fiction(title, author, isbn)
        return fiction

    def create_non_fiction(self, title, subject, level, isbn):
        non_fiction = Non_Fiction(title, subject, level, isbn)
        return non_fiction

    def add_book_to_user(self, book, email, rating = None):
        user = self.users.get(email)
        if user:
            user.read_book(book, rating)
            if not book in self.books:
                self.books[book] = 1
            self.books[book] += 1
            book.add_rating(rating)
                
        else:
            print("No user with email {email}!".format(email = email))

    def add_user(self, name, email, user_books = None):
        user = User(name, email)
        self.users[email] = user
        if user_books:
            for book in user_books:
                self.add_book_to_user(book, email)

    def print_catalog(self):
        for book in self.books:
            print(book)

    def print_users(self):
        for user in self.users.values():
            print(user)

    def most_read_book(self):
        max = 0
        for book_rating in self.books.values():
            if book_rating > max:
                max = book_rating
        return max

    def highest_rated_book(self):
        max = 0
        for book in self.books:
            if book.get_average_rating() > max:
                max = book.get_average_rating()

        for book in self.books:
            if book.get_average_rating() == max:
                return book

        return None

    def most_positive_user(self):
        max = 0
        for user in self.users.values():
            if user.get_average_rating() > max:
                max = user.get_average_rating()

        for user in self.users.values():
            if user.get_average_rating() == max:
                return user

        return None

    def get_n_most_read_bookds(self, n):
        most_read = []
        while n > 0:
            max = 0
            max_book = None
            for book in self.books:
                if self.books[book] > max and not book in most_read:
                    max = self.books[book]
                    max_book = book
            most_read.append(max_book)
            n -= 1
        return most_read

    def get_n_most_prolific_readers(self, n):
        most_read = []
        while n > 0:
            max = 0
            max_reader = None
            for reader in self.users.values():
                if len(reader.books) > max and not reader in most_read:
                    max = len(reader.books)
                    max_reader = reader
            most_read.append(max_reader)
            n -= 1
        return most_read
        

        
        
