#Output name
name=input("What is your name?  ").strip().title() 
print(name)
age= input("How old are you?  ")
print(f"You are {age} years old!")
#some cool asterisk shapes, maybe not cool yet haha
for i in range(4):
    print("*"*6)

for i in range(4):
    print("*"*(i+1))
#maybe not cool yet haha

#A program multiplies the value of x and displays it with "---" between them
x = (int(input("Enter the value of x  " )))
print(x,(x*2),(x*3),(x*4),(x*5),sep="---")

#This program calculates the bill, tip and total bill
Bill = eval(input("Input the amount of bill in USD  "))
Tip = eval(input("Enter Tip: as percentage of bill  "))
Tip = (Tip/100)*Bill
Total_Bill = Bill+Tip
print("TIP", Tip, "USD") 
print(f"TOTAL BILL {Total_Bill:,}", "USD")

#the foolowing code prints the total and average of three numbers 
x= eval(input("Enter the value of x  "))
y= eval(input("Enter the value of y  "))
z= eval(input("Enter the value of z  "))

average =(x+y+z)/3
total = x+y+z

print("Numbers enterd:",x,y,z)
print("TOTAL",total)
print("AVERAGE",average)

#loop for calculating square of numbers
for i in range (4):
    num = eval(input("Enter a number  "))
    print("The square of your number is,", num*num)
print("The loop is now done!") 

#Another program to input temp in degrees and output it in farenheit
temp= eval(input("Please enter the temperature in celcius "))
while temp <-273.15:
    temp = eval(input("That temperature is impossible! Please enter a valid value  "))
f_temp = 9/5*temp+32
print("In Farenheit that will be:", f_temp)

if f_temp > 212: 
    print("That temperature is above boiling point!")
if f_temp < 32:
    print("That temperature is below boiling point!") 

for i in range(1,6):
    print(i, "Gilbert")

# A countdown program
for i in range(5,0,-1):
    print(i,end=" ")
print("Blast off!!!")

import random

choice= random.choice(['Head','Tails'])
print(choice)

print()

#shuffle function from random, you can also use the from keyword to import a function from a module
cards =['jack','queen','king','ace']
random.shuffle(cards)
for card in cards:
    print(card)