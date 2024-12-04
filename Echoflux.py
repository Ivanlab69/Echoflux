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
    ╚══════╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚══════╝ ╚═════╝ ╚═╝  ╚═╝     ╚═════╝ ╚══════╝
    """
    stdscr.clear()  # Clear the screen
    stdscr.addstr(logo)  # Use addstr to print logo to screen
    stdscr.refresh()  # Refresh screen to display the changes

# Main menu
def display_main_menu(stdscr):
    options = [
        "1. Open Lynx Browser",
        "2. Open Terminal Shell",
        "3. Run Nmap Scan",
        "4. Brute Force Password",
        "5. Play Snake Game",
        "6. Open File Explorer",
        "7. Exit"
    ]
    
    current_option = 0
    while True:
        stdscr.clear()  # Clear the screen
        display_logo(stdscr)  # Display logo

        # Display menu options
        for i, option in enumerate(options):
            if i == current_option:
                stdscr.addstr(f"> {option}\n", curses.A_REVERSE)
            else:
                stdscr.addstr(f"  {option}\n")
        
        stdscr.refresh()

        key = stdscr.getch()  # Get key input
        if key == curses.KEY_DOWN:
            current_option = (current_option + 1) % len(options)
        elif key == curses.KEY_UP:
            current_option = (current_option - 1) % len(options)
        elif key == 10:  # Enter key pressed
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
                return  # Exit
        elif key == 27:  # Escape key pressed (exit)
            return  # Exit

# Open Lynx Browser
def start_lynx():
    print("Starting Lynx browser...")
    url = input("Enter URL to visit: ")
    os.system(f"lynx {url}")

# Open Terminal Shell
def start_shell():
    print("Opening shell terminal...")
    os.system("bash")  # Opens the standard bash shell

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

# Brute force password attack (educational purposes only)
def brute_force_attack():
    print("Starting Brute Force Attack... (for educational purposes)")
    target_user = input("Enter the username to target: ")
    wordlist_path = input("Enter the path to the wordlist file: ")

    if not os.path.exists(wordlist_path):
        print(f"Error: The wordlist file '{wordlist_path}' does not exist.")
        return

    with open(wordlist_path, 'r', encoding='utf-8') as file:
        passwords = file.readlines()

    passwords = [password.strip() for password in passwords]

    # Simulating password checking with hash comparison
    stored_password_hash = hashlib.sha256("secret_password".encode()).hexdigest()

    for count, password in enumerate(passwords, start=1):
        print(f"Attempt {count}: Trying password '{password}'...")
        input_password_hash = hashlib.sha256(password.encode()).hexdigest()
        if input_password_hash == stored_password_hash:
            print(f"[+] Success: Password found for user '{target_user}': {password}")
            return
        else:
            print(f"[-] Failed: '{password}' is incorrect.")
        time.sleep(0.5)

    print("[*] Brute force failed: No password found from the wordlist.")

# File Explorer
def open_file_explorer(stdscr):
    current_dir = os.getcwd()
    while True:
        stdscr.clear()  # Clear the screen
        display_logo(stdscr)  # Display logo
        stdscr.addstr(f"Current Directory: {current_dir}\n\n")

        # List files in current directory
        files = os.listdir(current_dir)
        for idx, file in enumerate(files):
            stdscr.addstr(f"{idx+1}. {file}\n")

        stdscr.refresh()

        key = stdscr.getch()  # Get key input
        if key == curses.KEY_DOWN:
            # Navigate down the list
            pass
        elif key == curses.KEY_UP:
            # Navigate up the list
            pass
        elif key == 10:  # Enter key pressed
            # Open file/folder (just simulating here)
            selected_file = files[0]  # Just for demonstration
            stdscr.clear()
            stdscr.addstr(f"Opening file {selected_file}\n")
            stdscr.refresh()
            time.sleep(1)
        elif key == 27:  # Escape key pressed (exit)
            break  # Exit

# Snake Game
def play_snake_game(stdscr):
    # Set up initial screen
    curses.curs_set(0)  # Hide cursor
    stdscr.nodelay(1)  # Non-blocking input
    stdscr.timeout(100)  # Set screen refresh timeout
    
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

        # Calculate new head of the snake
        if direction == curses.KEY_RIGHT:
            new_head = (snake[0][0], snake[0][1] + 1)
        elif direction == curses.KEY_LEFT:
            new_head = (snake[0][0], snake[0][1] - 1)
        elif direction == curses.KEY_UP:
            new_head = (snake[0][0] - 1, snake[0][1])
        elif direction == curses.KEY_DOWN:
            new_head = (snake[0][0] + 1, snake[0][1])

        snake.insert(0, new_head)
        if snake[0] == food:
            score += 1
            food = None
            while food is None:
                nf = (random.randint(1, height-1), random.randint(1, width-1))
                food = nf if nf not in snake else None
            window.addch(food[0], food[1], curses.ACS_PI)
        else:
            tail = snake.pop()
            window.addch(tail[0], tail[1], ' ')

        window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)

        # Check for collision with wall or self
        if (snake[0][0] in [0, height] or 
            snake[0][1] in [0, width] or 
            snake[0] in snake[1:]):
            curses.endwin()
            quit()
    
    curses.endwin()

# Main entry function
def main(stdscr):
    curses.curs_set(0)  # Hide cursor
    stdscr.nodelay(1)  # Make getch non-blocking
    stdscr.timeout(100)  # Set timeout for screen updates

    while True:
        display_main_menu(stdscr)

if __name__ == "__main__":
    curses.wrapper(main)
