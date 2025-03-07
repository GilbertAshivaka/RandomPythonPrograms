class Book:
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.__price = price
        self.__discount = None
    
    def set_discount(self, discount):
        self.__discount = discount

    def get_price(self):
        if self.__discount:
            return self.__price * (1-self.__discount)
        return self.__price


    def __repr__(self):
        return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.get_price()}"


single_book = Book('Social Psychology', 1, 'Keltner', 200)
bulk_books = Book('Social Psychology', 25, 'Keltner', 200)
bulk_books.set_discount(0.20)

print(single_book)
print(single_book.get_price())
print(bulk_books)
print(bulk_books.get_price())

