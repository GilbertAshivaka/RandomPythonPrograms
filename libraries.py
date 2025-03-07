
#To be a little defensive to ensure that the user enters the right arguments
import sys
if len(sys.argv) <2:
    exit("Too few arguments. Type in something ")
elif len(sys.argv) >5:
    exit("Too many arguments.")
#The -1 prints the list without the last element
for arg in sys.argv[1:-1:]: 
    print("Hello, my name is",arg)

print()
print()

try:
    import sys
    print("Hello, my name is",sys.argv[1])
except IndexError:
    print("Too few arguments.Type something in  ")





