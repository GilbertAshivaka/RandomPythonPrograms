#print meow and also validate the data that the user enters
words = input("Enter the word to be displayed.  ")

while True:
    i = eval(input("How many times do you want the word to be printed?  "))
    if i > 0:
        break
    else: 
        print("Invalid input!")
        

for _ in range(i):
    print(words)

#Defining functions 
def main():
    number = get_number()
    hello(number)


def get_number():
    while True:
        i = eval(input("How many times do you want the word displayed?  "))
        if i > 0:
            break
        else:
            print("Invalid input, Try Again")
    return i

word = input("Enter the word you want dispayed.  ")

def hello(i):
    for _ in range(i):
        print(word)

main()
    

    