import moviepy
import moviepy.editor
import colorama
from colorama import Fore, Style, init

def Conventer():
    file_pach = input(Fore.LIGHTCYAN_EX + "Enter File Path ! ")
    if file_pach:
        print(f"You choose file : {file_pach} ")
    else:
        print("File dont choosed! ")

    video = moviepy.editor.VideoFileClip(file_pach)
    audio = video.audio
    audio.write_audiofile('new_audio.mp3')
