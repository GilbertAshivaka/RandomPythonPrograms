'''
The following is a library management system.
'''

class Library:
    def __init__(self, books):
        self.books = books 

    def avail_books(self):
        print('Our library can offer you the following:  ')
        print('===========================================================')
        for book, borrower in self.books.items():
            if borrower == 'Free':
                print(book)

    def lend_book(self, requested_book, name):
        if self.books[requested_book] == 'Free':
            print(f'{requested_book} has been marked as borrowed by: {name}')
            self.books[requested_book] = name
            return True
        else:
            print(f'Sorry, {requested_book} is currently on loan to: {self.books[requested_book]}')
            return False
        
    def return_book(self, returned_book):
        self.books[returned_book] == 'Free'
        print(f'Thanks for returning {returned_book}.')

class Student():
    def __init__(self, name, library):
        self.name = name 
        self.books = []
        self.library = library

    def view_borrowed(self):
        if not self.books:
            print('You haven\'t borrowed any books')
        else:
            for book in self.books:
                print(book)
    

    def request_book(self):
        book = input('Enter the title of the book you\'d like to request:  ')
        if self.library.lend_book(book, self.name):
            self.books.append(book)
    

    def return_book(self):
        book = input('Enter the title of the book you\'d like to return:  ')
        if book in self.books:
            self.library.return_book(book)
        else: 
            print('You have not borrowed that book, check the title or try another.')

def get_name():
    stud_name = input('Enter your name: ')
    return stud_name.title()

def create_lib():
    books = {
        'The last batle': 'Free',
        'The hunger games': 'Free',
        'Cracking the coding interview': 'Free'
    }

    library = Library(books)
    student = Student(get_name(), library)


    while True:
        print('''
            ==========LIBRARY MENU===========
           1. Display Available Books
           2. Borrow a Book
           3. Return a Book
           4. View Your Books
           5. Exit
           ''')
        
        choice = eval(input('Enter your choice:  '))
        if choice == 1:
            print()
            library.avail_books()
        if choice == 2:
            print()
            student.request_book()
        if choice == 3:
            print()
            student.return_book()
        if choice == 4:
            print()
            student.view_borrowed()
        if choice == 5:
            print()
            print('Goodbye!!')
            exit()

if __name__ == '__main__':
    create_lib()


    
