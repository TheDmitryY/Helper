import random, time
import colorama
from colorama import Fore, Style, init

def Password_Menu():
    print(Fore.LIGHTCYAN_EX + "Welcome to Password Generator ! \n")
    Password_Generate()
def Password_Generate():
    lower_a = 'abcdefghijklmnopqrstuvxyz'
    upper_a = lower_a.upper()
    numbers = "0123456789"
    symbols = "@#*^!?()$&+"
    length = 12
    repeating = 1
    p = lower_a + upper_a + numbers + symbols
    option = input(Fore.LIGHTYELLOW_EX + "[$] You wanna change generating settings? [y/n] ")

    if option == "y":
        print(Fore.LIGHTYELLOW_EX + " [1] Change password length")
        print(Fore.LIGHTYELLOW_EX + " [2] Change repeating password")
        choice = int(input(Fore.LIGHTYELLOW_EX + "\n [$] Choose action --> "))

        if choice == 1:
            length = int(input(Fore.LIGHTYELLOW_EX + " [$] Enter password length: \n"))
            for _ in range(repeating):
                complete = ''.join(random.sample(p, length))
                print(Fore.LIGHTYELLOW_EX + " [$] Generated Password: ", complete + "\n")
                time.sleep(0.5)

        elif choice == 2:
            repeating = int(input(Fore.LIGHTYELLOW_EX + " [$] Enter password repeating: "))
            for _ in range(repeating):
                complete = "".join(random.sample(p, length))
                print(Fore.LIGHTYELLOW_EX + " [$] Generated Password: ", complete + "\n")
                time.sleep(0.5)

    elif option == "n":
        for _ in range(repeating):
            complete = "".join(random.sample(p, length))
            print(Fore.LIGHTYELLOW_EX + " [$] Generated Password: ", complete + "\n")
            time.sleep(0.5)