def main():
    x = get_num("Enter a number  ")
    print(f"The number you entered is {x}.")


def get_num(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
        
        
main()