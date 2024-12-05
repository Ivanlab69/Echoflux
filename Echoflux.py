import os
import subprocess
import time
import hashlib
import nmap
import curses
import random

# Display logo as ASCII art
def display_logo(stdscr):
    logo = """
    ███████╗ ██████╗██╗  ██╗ ██████╗ ███████╗██╗     ██╗   ██╗██╗  ██╗     ██████╗ ███████╗
    ██╔════╝██╔════╝██║  ██║██╔═══██╗██╔════╝██║     ██║   ██║╚██╗██╔╝    ██╔═══██╗██╔════╝
    █████╗  ██║     ███████║██║   ██║█████╗  ██║     ██║   ██║ ╚███╔╝     ██║   ██║███████╗
    ██╔══╝  ██║     ██╔══██║██║   ██║██╔══╝  ██║     ██║   ██║ ██╔██╗     ██║   ██║╚════██║
    ███████╗╚██████╗██║  ██║╚██████╔╝██║     ███████╗╚██████╔╝██╔╝ ██╗    ╚██████╔╝███████║
    ╚══════╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚══════╝╚═════╝ ╚═╝  ╚═╝     ╚═════╝ ╚══════╝
    """
    stdscr.clear()
    stdscr.addstr(logo, curses.color_pair(1))
    stdscr.refresh()

# Main menu
def display_main_menu(stdscr):
    options = [
        "1. Open Lynx Browser",
        "2. Open Terminal Shell (Wine CMD)",
        "3. Run Nmap Scan",
        "4. Brute Force Password",
        "5. Play Snake Game",
        "6. Open File Explorer",
        "7. Exit"
    ]
    
    current_option = 0
    while True:
        stdscr.clear()
        display_logo(stdscr)

        # Display menu options
        for i, option in enumerate(options):
            if i == current_option:
                stdscr.addstr(f"> {option}\n", curses.color_pair(2))
            else:
                stdscr.addstr(f"  {option}\n", curses.color_pair(1))
        
        stdscr.refresh()

        key = stdscr.getch()
        if key == curses.KEY_DOWN:
            current_option = (current_option + 1) % len(options)
        elif key == curses.KEY_UP:
            current_option = (current_option - 1) % len(options)
        elif key == 10:  # Enter key
            if current_option == 0:
                start_lynx()
            elif current_option == 1:
                start_shell()
            elif current_option == 2:
                run_nmap()
            elif current_option == 3:
                brute_force_attack()
            elif current_option == 4:
                play_snake_game(stdscr)
            elif current_option == 5:
                open_file_explorer(stdscr)
            elif current_option == 6:
                return
        elif key == 27:  # Escape key
            return

# Open Lynx Browser
def start_lynx():
    print("Starting Lynx browser...")
    url = input("Enter URL to visit: ")
    os.system(f"lynx {url}")

# Open Wine CMD terminal
def start_shell():
    print("Opening Wine cmd terminal...")
    os.system("wine cmd")  # Launches Wine's Command Prompt

# Run Nmap Scan
def run_nmap():
    print("Starting Nmap scan...")
    target = input("Enter the IP address or hostname for Nmap scan: ")
    scanner = nmap.PortScanner()
    print(f"Scanning {target}...")
    scanner.scan(target, '1-1024')
    for host in scanner.all_hosts():
        print(f"Host: {host} ({scanner[host].hostname()})")
        print(f"State: {scanner[host].state()}")
        for protocol in scanner[host].all_protocols():
            ports = scanner[host][protocol].keys()
            for port in ports:
                print(f"Port: {port}, State: {scanner[host][protocol][port]['state']}")

# Brute Force Password (educational purposes only)
def brute_force_attack():
    print("Starting Brute Force Attack...")
    target_user = input("Enter the username to target: ")
    wordlist_path = input("Enter the path to the wordlist file: ")

    if not os.path.exists(wordlist_path):
        print(f"Error: The wordlist file '{wordlist_path}' does not exist.")
        return

    with open(wordlist_path, 'r', encoding='utf-8') as file:
        passwords = [line.strip() for line in file]

    stored_password_hash = hashlib.sha256("secret_password".encode()).hexdigest()

    for count, password in enumerate(passwords, start=1):
        print(f"Attempt {count}: Trying password '{password}'...")
        input_password_hash = hashlib.sha256(password.encode()).hexdigest()
        if input_password_hash == stored_password_hash:
            print(f"Success: Password found for user '{target_user}': {password}")
            return
        time.sleep(0.5)

    print("Brute force failed: No password found.")

# File Explorer
def open_file_explorer(stdscr):
    current_dir = os.getcwd()
    while True:
        stdscr.clear()
        display_logo(stdscr)
        stdscr.addstr(f"Current Directory: {current_dir}\n\n", curses.color_pair(1))

        files = os.listdir(current_dir)
        for idx, file in enumerate(files):
            stdscr.addstr(f"{idx+1}. {file}\n", curses.color_pair(1))

        stdscr.refresh()

        key = stdscr.getch()
        if key == 27:  # Escape key
            break

# Snake Game
def play_snake_game(stdscr):
    curses.curs_set(0)
    stdscr.timeout(100)

    height, width = stdscr.getmaxyx()
    window = curses.newwin(height, width, 0, 0)
    window.keypad(1)

    snake = [(height // 2, width // 4), (height // 2, width // 4 - 1), (height // 2, width // 4 - 2)]
    food = (height // 2, width // 2)
    window.addch(food[0], food[1], curses.ACS_PI)

    direction = curses.KEY_RIGHT
    score = 0

    while True:
        next_key = window.getch()
        direction = direction if next_key == -1 else next_key

        new_head = (snake[0][0], snake[0][1] + (1 if direction == curses.KEY_RIGHT else -1))
        snake.insert(0, new_head)

        if snake[0] == food:
            score += 1
            food = None
            while food is None:
                nf = (random.randint(1, height - 2), random.randint(1, width - 2))
                food = nf if nf not in snake else None
            window.addch(food[0], food[1], curses.ACS_PI)
        else:
            tail = snake.pop()
            window.addch(tail[0], tail[1], ' ')

        window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)

        if (snake[0][0] in [0, height - 1] or snake[0][1] in [0, width - 1] or snake[0] in snake[1:]):
            break

    curses.endwin()

# Main entry function
def main(stdscr):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.curs_set(0)
    display_main_menu(stdscr)

if __name__ == "__main__":
    curses.wrapper(main)

