length= eval(input("How many asterisks do you want the length of the rectangle to have?  "))
width= eval(input("How many asterisks do you want the width of the rectangle to have?  "))

if length < width:
    print("Interchange the values to make it look like a normal rectangle.")

l=length-2
w=width-2

for i in range(1):
    print("*"*length)


for i in range(w):
    print("*","*", sep=" "*l)

for i in range(1):
    print("*"*length) 



