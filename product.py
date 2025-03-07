from os import name


class Product:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price
    

    def get_price(self, n):
        if 10<n<=99:
            return n*self.price*0.90
        elif n>=100:
            return n*self.price*0.8
        
    def make_purchase(self, n):
        return self.amount-n

    def __str__(self):
        return f"Product: {self.name}, Quantity: {n}, Price: {self.get_price()}"

n = eval(input("Enter the amount of items you want to buy:  "))


product = Product("Books", 500, 100)

print("You will pay: ",product.get_price(n))
print("Books still in store:  ",product.make_purchase(n))