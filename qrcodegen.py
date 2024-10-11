import qrcode
import  os
import colorama
from colorama import Fore, Style, init

def Code_Menu():
    print(Fore.LIGHTGREEN_EX + "Welcome to QR-Code generator ! \n")
    Create_Code()

def Create_Code():
    text = input(Fore.LIGHTGREEN_EX + "Enter text for QR-Code : ")
    filename = input(Fore.LIGHTGREEN_EX + "Enter file name for saving" + ".png : ")
    img = qrcode.make(text)
    img.save(filename)
    print(f'QR-Code succesful created and saved to {filename} file ')
    os.startfile(filename)

