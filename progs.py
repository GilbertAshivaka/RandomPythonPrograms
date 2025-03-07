#This program prints A,B,then alternates between C and D then E 
print("A")
print("B")
for i in range(5):
    print("C", end="")
    print("D", end="")
print("\n","E", sep="")

#If we want it to print five Cs then 5 Ds we could make it look like this
print("A")
print("B")
for i in range(5):
    print("C",end="")
print("\n",end="")
for i in range(5):
     print("D",end="")
print("\n","E", sep="")

#Print hello and your name 5 times
name= input("What is your name?  ")
for i in range(5):
    print(i+1, "---Hello",name)

#A program for printing a number and its square 
for i in range(1,21):
    print(i,"---", i*i)

for i in range(8,90,3):
    print(i," ",sep=",", end="")

print("\n",end="")
for i in range(100,0,-2):
    print(i," ",sep=",", end="")



for i in range(10):
    print("A",end="")
for i in range(7):
    print("B",end="")
for i in range(4):
    print("C",end="")
    print("D",end="")
print("E",end="")
for i in range(6):
    print("F",end="")
print("G")

name= input("What is your name?  ")
times= eval(input("How many times do you want your name displayed?  "))
for i in range(times):
    print(name)






