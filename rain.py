import random
import time
from string import digits

def rain_characters(width, height, chars, speed):
    columns = [0] * width

    while True:
        for x in range(width):
            if columns[x] == 0 or random.uniform(0, 1) < 0.1:
                columns[x] = random.randint(1, height)
            else:
                columns[x] -= 1

        for y in range(height):
            for x in range(width):
                if columns[x] >= y:
                    print(random.choice(chars), end='')
                else:
                    print(' ', end='')
            print()

        time.sleep(speed)
        print('\033c')  # Clears the screen

# Adjust the parameters as per your preference
rain_characters(width=160, height=30, chars=digits, speed=0.1)
