#A program to print fibonacci sequence
def fibo(n):
    if n <=1:
        return n
    else:
        return(fibo(n-1)+fibo(n-2))

nterms=eval(input("Enter the number of terms you want displayed  "))

#check if the number of terms is valid and keeps prompting until they enter a valid input
while nterms < 0:
    eval(input("Please enter a positive integer  "))

else:
    print("Fibonacci sequence")
    for i in range(nterms):
        print(fibo(i)," ",sep=",",end="")


    
