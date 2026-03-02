from os import system
import sys


def deleteScreen():
    if sys.platform == "linux" or sys.platform == "darwin":
        system("clear")
    else:
        system("cls")


def pauseScreen():
    if sys.platform == "linux" or sys.platform == "darwin":
        pause = input("\nPress enter to continue...")
    else:
        system("pause")
