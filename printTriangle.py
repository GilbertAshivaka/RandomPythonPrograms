h = int(input("How wide do you want the triangle to be?.... "))

for i in range(h+1):
    print(" "*(h-i) + "*"*(2*i-1))