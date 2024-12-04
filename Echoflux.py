import os
import time
import hashlib
import nmap
import curses
import subprocess
import random

# Display logo as ASCII art
def display_logo():
    logo = """
    ███████╗ ██████╗██╗  ██╗ ██████╗ ███████╗██╗     ██╗   ██╗██╗  ██╗     ██████╗ ███████╗
    ██╔════╝██╔════╝██║  ██║██╔═══██╗██╔════╝██║     ██║   ██║╚██╗██╔╝    ██╔═══██╗██╔════╝
    █████╗  ██║     ███████║██║   ██║█████╗  ██║     ██║   ██║ ╚███╔╝     ██║   ██║███████╗
    ██╔══╝  ██║     ██╔══██║██║   ██║██╔══╝  ██║     ██║   ██║ ██╔██╗     ██║   ██║╚════██║
    ███████╗╚██████╗██║  ██║╚██████╔╝██║     ███████╗╚██████╔╝██╔╝ ██╗    ╚██████╔╝███████║
    ╚══════╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚══════╝ ╚═════╝ ╚═╝  ╚═╝     ╚═════╝ ╚══════╝
    """
    print(logo)

# Help menu
def display_help():
    print("""
    Echoflux OS Help Menu:
    1. Open Lynx Browser
    2. Open Terminal Shell
    3. Run Nmap Scan
    4. Run Brute Force Attack
    5. Play Snake Game
    6. Exit
    """)

# Start Lynx Browser
def start_lynx():
    print("Starting Lynx browser...")
    url = input("Enter URL to visit: ")
    os.system(f"lynx {url}")

# Start Terminal Shell
def start_shell():
    print("Opening shell terminal...")
    os.system("bash")

# Run Nmap Scan
def run_nmap():
    print("Starting Nmap scan...")
    target = input("Enter the IP address or hostname for Nmap scan: ")
    scanner = nmap.PortScanner()
    print(f"Scanning {target}...")
    scanner.scan(target, '1-1024')  # Scans ports 1-1024
    print(scanner.all_hosts())
    for host in scanner.all_hosts():
        print(f"Host: {host}")
        print(f"State: {scanner[host].state()}")
        for protocol in scanner[host].all_protocols():
            print(f"Protocol: {protocol}")
            lport = scanner[host][protocol].keys()
            for port in lport:
                print(f"Port: {port}, State: {scanner[host][protocol][port]['state']}")
    print("Scan completed.")

# Brute Force Logic
def check_password(user, password):
    stored_password_hash = hashlib.sha256("secret_password".encode()).hexdigest()
    input_password_hash = hashlib.sha256(password.encode()).hexdigest()
    return stored_password_hash == input_password_hash

def brute_force_attack():
    print("Starting brute force attack...")
    wordlist = input("Enter the path to the wordlist file: ")
    if not os.path.exists(wordlist):
        print(f"Error: The wordlist file '{wordlist}' does not exist.")
        return
    with open(wordlist, 'r') as file:
        passwords = file.readlines()

    for password in passwords:
        password = password.strip()
        print(f"Trying password: {password}...")
        if check_password("admin", password):
            print(f"Password found: {password}")
            return
        time.sleep(0.1)
    print("Password not found.")

# Simple Snake Game
def play_snake_game(stdscr):
    snake_logo = """
    ███████╗██╗███╗   ██╗██████╗ ███████╗██╗   ██╗
    ██╔════╝██║████╗  ██║██╔══██╗██╔════╝██║   ██║
    █████╗  ██║██╔██╗ ██║██████╔╝███████╗╚██╗ ██╔╝
    ██╔══╝  ██║██║╚██╗██║██╔═══╝ ██╔══╝   ╚████╔╝
    ███████╗██║██║ ╚████║██║     ███████╗   ╚██╔╝
    ╚══════╝╚═╝╚═╝  ╚═══╝╚═╝     ╚══════╝    ╚═╝
    """
    stdscr.clear()
    stdscr.addstr(0, 0, snake_logo)
    stdscr.refresh()
    time.sleep(1)

    # Initialize snake and game parameters
    height, width = stdscr.getmaxyx()
    win = curses.newwin(height, width, 0, 0)
    win.keypad(1)
    curses.curs_set(0)
    win.timeout(100)

    snake_x = width // 4
    snake_y = height // 2
    snake = [
        [snake_y, snake_x],
        [snake_y, snake_x - 1],
        [snake_y, snake_x - 2]
    ]

    food = [height // 2, width // 2]
    win.addch(food[0], food[1], curses.ACS_PI)

    key = curses.KEY_RIGHT
    while True:
        next_key = win.getch()
        key = key if next_key == -1 else next_key

        if snake[0][0] in [0, height] or \
           snake[0][1] in [0, width] or \
           snake[0] in snake[1:]:
            curses.endwin()
            quit()

        new_head = [snake[0][0], snake[0][1]]

        if key == curses.KEY_DOWN:
            new_head[0] += 1
        if key == curses.KEY_UP:
            new_head[0] -= 1
        if key == curses.KEY_LEFT:
            new_head[1] -= 1
        if key == curses.KEY_RIGHT:
            new_head[1] += 1

        snake.insert(0, new_head)

        if snake[0] == food:
            food = None
            while food is None:
                new_food = [
                    random.randint(1, height - 1),
                    random.randint(1, width - 1)
                ]
                food = new_food if new_food not in snake else None
            win.addch(food[0], food[1], curses.ACS_PI)
        else:
            tail = snake.pop()
            win.addch(tail[0], tail[1], ' ')

        win.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)

# Main Menu Interface
def main_menu():
    os.system('clear')  # Clears the terminal screen
    display_logo()
    while True:
        print("\nEchoflux OS - Main Menu:")
        print("1. Help")
        print("2. Start Lynx Browser")
        print("3. Start Shell")
        print("4. Run Nmap Scan")
        print("5. Brute Force Attack")
        print("6. Play Snake Game")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_help()
        elif choice == "2":
            start_lynx()
        elif choice == "3":
            start_shell()
        elif choice == "4":
            run_nmap()
        elif choice == "5":
            brute_force_attack()
        elif choice == "6":
            curses.wrapper(play_snake_game)
        elif choice == "7":
            print("Exiting Echoflux OS...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()

