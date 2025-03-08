import random
import time

def rain_characters(width, height, num_columns, speed):
    columns = [0] * num_columns

    while True:
        for x in range(num_columns):
            if columns[x] <= 0:
                columns[x] = random.randint(1, height)
            else:
                columns[x] -= 1

        for y in range(height):
            for x in range(width):
                if x % (width // num_columns) == 0:
                    if columns[x // (width // num_columns)] == y:
                        print(random.randint(0, 9), end='')
                    else:
                        print(' ', end='')
            print()

        time.sleep(speed)
        print('\033c')  # Clears the screen

# Adjust the parameters as per your preference
rain_characters(width=80, height=30, num_columns=20, speed=0.1)


