class Parentclass:
    def call_me(self):
        print("I am the parent class.")

class Childclass(Parentclass):
    def call_me(self):
        print("I am the childclass.")
        super().call_me()



pobj = Parentclass()
pobj.call_me()

cobj = Childclass()
cobj.call_me()