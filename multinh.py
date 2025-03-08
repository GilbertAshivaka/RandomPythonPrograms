class Car:
    def start(self):
        print("Start the car.")

    def go(self):
        print("Going.")

class Flyable:
    def start(self):
        print("Start the flying object.")

    def fly(self):
        print("Flying.")

class FlyingCar(Car, Flyable):
    def start(self):
        super().start()



if __name__ == "__main__":
    car = FlyingCar()
    car.start()
    print(FlyingCar.__mro__)