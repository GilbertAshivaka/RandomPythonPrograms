#this code take input from the user, removes space around it and puts it in title case and outputs it
print(name=input("What is your name?")).strip.title
#it could othwerwise be written this way
print(input("What is your name?"))
name=input()
print(name)  
name.strip
name.title

#Another program to input temp in degrees and output it in farenheit
temp= eval(input("Please enter the temperature in celcius "))
f_temp = 9/5*temp+32
print("In Farenheit that will be:", f_temp)
if f_temp > 212: 
    print("That temperature is above boiling point!")
if f_temp < 32:
    print("That temperature is below boiling point!") 

#the foolowing code prints the total and average of three numbers 
x= eval(input())
y= eval(input())
z= eval(input())

average =(x+y+z)/3
total = x+y+z 

x =print(eval(input("Enter the value of x" )))
print(x,2*x,3*x,4*x,5*x,sep="---")

#program to output total bill and tip
Bill = print(eval(input("Input the amount of bill in USD")))
Tip = print(eval(input("Enter Tip: as percentage of bill")))
Tip = (Tip/100)*Bill
Total_Bill = Bill+Tip
print(Tip+"USD", Bill+"ÜSD") 

#using a for loop to output a square of a number
for i in range (4):
    num = eval(input("Enter a number"))
    print("The square of your number is,", num*num)
print("The loop is now done") 

#This program prints the "*" symbol in a rectangle
for i in range(4):
    print("*"*6)

#This other one prints it in a triangle 
for i in range(4):
    print("*"*(i+1)) 