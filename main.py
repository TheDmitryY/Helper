from func import  Logo, Menu,Clear
from colorama import Fore,Style, init



if __name__ == '__main__':
    while True:
        Logo()
        repeat = input(Fore.LIGHTBLUE_EX + "\n[$] Your wanna repeat? [ Yes/No] :  ")
        if repeat != "Yes":
            Clear()
            break