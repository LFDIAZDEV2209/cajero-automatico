from os import system
import sys


def deleteScreen():
    """Delete the screen"""
    if sys.platform == "linux" or sys.platform == "darwin":
        system("clear")
    else:
        system("cls")


def pauseScreen():
    """Pause the screen"""
    if sys.platform == "linux" or sys.platform == "darwin":
        pause = input("\nPress enter to continue...")
    else:
        system("pause")
