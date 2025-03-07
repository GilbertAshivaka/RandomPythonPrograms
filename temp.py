temp = 0
while temp != -1000:
    temp = eval(input("Enter the temperature in celcius  "))
    if temp != -1000:
        print("In Farenheit, that will be:",9/5*temp+32 )
    else: 
        print("BYE")
              



while True:
    temp = eval(input("Enter temperature in celcius  "))
    if temp !=-1000:
        print("In Farenheit that will be:", 9/5*temp+32)
    else:
        print("That's not right. Bye!")
        break



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









