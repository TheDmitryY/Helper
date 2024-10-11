import colorama
from colorama import Style, Fore, init
import os
from mp3 import Conventer
from  password import Password_Menu;
from qrcodegen import Code_Menu
from audiobook import  Book_Menu

init()

def Logo():
    print(Fore.LIGHTCYAN_EX + "██╗  ██╗███████╗██╗     ██████╗ ███████╗██████╗ ")
    print(Fore.LIGHTCYAN_EX + "██║  ██║██╔════╝██║     ██╔══██╗██╔════╝██╔══██╗")
    print(Fore.LIGHTCYAN_EX + "███████║█████╗  ██║     ██████╔╝█████╗  ██████╔╝")
    print(Fore.LIGHTCYAN_EX + "██╔══██║██╔══╝  ██║     ██╔═══╝ ██╔══╝  ██╔══██╗")
    print(Fore.LIGHTCYAN_EX + "██║  ██║███████╗███████╗██║     ███████╗██║  ██║")
    print(Fore.LIGHTCYAN_EX + "╚═╝  ╚═╝╚══════╝╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝")
    print(Fore.LIGHTWHITE_EX + "                                  by HorekiSun")
    Menu()


def Menu():
    print(Fore.LIGHTCYAN_EX + " [1] QR-Code Generator")
    print(Fore.LIGHTCYAN_EX + " [2] MP3 Convertor")
    print(Fore.LIGHTCYAN_EX + " [3] Audio Book Convertor")
    print(Fore.LIGHTCYAN_EX + " [4] Password Generator")
    print(Fore.LIGHTCYAN_EX + " [5] About")
    choise = int(input(Fore.LIGHTCYAN_EX + "\n [$] Choose action -->  "))
    Clear()
    if choise == 1:
        Code_Menu()
    elif choise == 2:
        Clear()
        Conventer()
    elif choise == 3:
        Clear()
        Book_Menu()
    elif choise == 4:
        Clear()
        Password_Menu()
    elif choise == 5:
        Clear()
        print(Fore.LIGHTMAGENTA_EX + "Helper is a console program that helps manage the system, which has built-in utilities.")
        print(Fore.LIGHTMAGENTA_EX + "We support user ratings and ideas. You can write to us in case of an idea, and other useful")
        print(Fore.LIGHTMAGENTA_EX + "\nAuthor : HorekiSun")
        print(Fore.LIGHTMAGENTA_EX + "GitHub : TheDmitryY")
        print(Fore.LIGHTMAGENTA_EX + "Telegram : horekisun")



def Clear():
    os.system('cls')