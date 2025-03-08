from abc import ABC, abstractmethod

class CurrencyConverter(ABC):
    def convert(self, from_amount, to_amount, amount):
        pass



class FXConverter(CurrencyConverter):
    def convert(self, from_amount, to_amount, amount):
        print("Converting currency using FX API.")
        print(f"{amount} {from_amount} = {amount*140} {to_amount}")

        return amount*140


class AlphaConverter(CurrencyConverter):
    def convert(self, from_amount, to_amount, amount):
        print("Converting currency using Alpha API.")
        print(f"{amount} {from_amount} = {amount*140} {to_amount}")

        return amount*1.2
    


class App:
    def __init__(self, converter: CurrencyConverter):
        self.converter = converter

    def start(self):
        self.converter.convert("USD", "KES", 100)



if __name__ == "__main__":
    converter = FXConverter()
    app = App(converter)
    app.start()


        



'''This following version of the code does not use the dependency inversion SOLID PRINCIPLE'''




'''
    In this case the App class depends on the FXConverter class and not the other way
    To make it better code the FXConverter should depend on the App class.
'''
class FXConverter:
    def convert(self, from_amount, to_amount, amount):
        print(f"{amount} {from_amount} = {amount*140} {to_amount}")
        return amount*140
    


class App():
    def start(self):
        converter = FXConverter()
        converter.convert("USD", "KES", 100)


if __name__ == "__main__":
    app = App()
    app.start()
