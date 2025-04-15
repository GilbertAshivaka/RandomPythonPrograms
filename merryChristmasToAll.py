import time
import os
import random
import sys
from itertools import cycle

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Colors:
    GREEN = '\033[32m'
    BRIGHT_GREEN = '\033[92m'
    RED = '\033[31m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    RESET = '\033[0m'

def print_with_delay(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

class ChristmasTree:
    def __init__(self):
        self.ornaments = ['o', '*', '@', '•', '✦']
        self.colors = [Colors.RED, Colors.YELLOW, Colors.BLUE, Colors.MAGENTA, Colors.CYAN]
        self.height = 15

    def generate_tree(self, frame):
        tree = []
        # Star at the top with animation
        star_frames = ['⋆', '★', '☆', '✯']
        tree.append(f"{' ' * (self.height+2)}{Colors.YELLOW}{star_frames[frame % len(star_frames)]}{Colors.RESET}")
        
        for i in range(self.height):
            spaces = ' ' * (self.height - i)
            if i == 0:
                tree.append(f"{spaces}{Colors.BRIGHT_GREEN}^{Colors.RESET}")
                continue
                
            line = ''
            for j in range(2*i + 1):
                if random.random() < 0.2:  # 20% chance for an ornament
                    ornament = random.choice(self.ornaments)
                    color = random.choice(self.colors)
                    line += f"{color}{ornament}{Colors.RESET}"
                else:
                    line += f"{Colors.BRIGHT_GREEN}^{Colors.RESET}"
            
            tree.append(f"{spaces}{line}")
        
        # Tree trunk
        trunk_height = 3
        trunk_width = 5
        for _ in range(trunk_height):
            spaces = ' ' * (self.height - trunk_width//2)
            tree.append(f"{spaces}{Colors.RED}|||{Colors.RESET}")
        
        return tree

def print_presents(frame):
    presents = [
        f"{Colors.RED}   ╔════╗ {Colors.BLUE}╔══╗{Colors.RESET}",
        f"{Colors.RED}   ║    ║ {Colors.BLUE}║  ║{Colors.RESET}",
        f"{Colors.RED}╔══╩════╩═{Colors.BLUE}╩══╩══╗{Colors.RESET}",
        f"{Colors.RED}║             {Colors.BLUE}   ║{Colors.RESET}",
        f"{Colors.RED}╚═════════════{Colors.BLUE}═══╝{Colors.RESET}"
    ]
    
    # Add animated bow
    bow_frames = [
        "▽", "▼", "▽", "▲"
    ]
    
    for i, line in enumerate(presents):
        if i == 0:
            print(f"{line}{Colors.YELLOW}{bow_frames[frame % len(bow_frames)]}{Colors.RESET}")
        else:
            print(line)

def print_snowflakes(frame, width):
    snowflakes = ['❄', '❅', '❆']
    snow_line = ''
    for i in range(width):
        if random.random() < 0.1:  # 10% chance for snowflake
            snow_line += random.choice(snowflakes)
        else:
            snow_line += ' '
    print(f"{Colors.WHITE}{snow_line}{Colors.RESET}")

def print_text(frame):
    text_colors = cycle([Colors.RED, Colors.GREEN, Colors.YELLOW, Colors.BLUE, Colors.MAGENTA, Colors.CYAN])
    text = [
        "╔╦╗╔═╗╦═╗╦═╗╦ ╦",
        "║║║║╣ ╠╦╝╠╦╝╚╦╝",
        "╩ ╩╚═╝╩╚═╩╚═ ╩ ",
        "",
        "╔═╗╦ ╦╦═╗╦╔═╗╔╦╗╔╦╗╔═╗╔═╗",
        "║  ╠═╣╠╦╝║╚═╗ ║ ║║║╠═╣╚═╗",
        "╚═╝╩ ╩╩╚═╩╚═╝ ╩ ╩ ╩╩ ╩╚═╝"
    ]
    
    for line in text:
        color = next(text_colors)
        print(f"{' ' * 10}{color}{line}{Colors.RESET}")

def main():
    frame = 0
    tree = ChristmasTree()
    
    try:
        while True:
            clear_screen()
            
            # Print animated snowflakes at the top
            print_snowflakes(frame, 50)
            
            # Generate and print the tree
            current_tree = tree.generate_tree(frame)
            for line in current_tree:
                print(line)
            
            print()  # Empty line
            print_text(frame)
            print()  # Empty line
            print_presents(frame)
            
            time.sleep(0.2)  # Control animation speed
            frame += 1

    except KeyboardInterrupt:
        clear_screen()
        print(f"{Colors.GREEN}Happy Holidays!{Colors.RESET}")

if __name__ == "__main__":
    main()