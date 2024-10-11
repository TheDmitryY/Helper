import pyttsx3
import colorama
from colorama import Fore, Style, init
import os

def Book_Menu():
    print(Fore.LIGHTCYAN_EX + "Welcome to AudioBook Convertor!")
    Get_Book()
def Get_Book():
    filename = input(Fore.LIGHTYELLOW_EX + "Enter file path : ")
    succes = input(Fore.LIGHTYELLOW_EX + "Enter saved file name [file.mp3] : ")
    with open("%s" % filename, "r") as book:
        book_text = book.readlines()
    engine = pyttsx3.init()
    for i in book_text:

        engine.save_to_file(i, succes)
        engine.runAndWait()
        os.startfile(succes)
