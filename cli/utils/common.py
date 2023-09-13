import os
from string import Template


def print_info(message: str):
    """
    Prints a message in cyan color.
    """
    print("\033[36m" + message + "\033[0m")


def print_error(message: str):
    """
    Prints a message in red color.
    """
    print("\033[91m" + message + "\033[0m")


def print_success(message: str):
    """
    Prints a message in green color.
    """
    print("\033[92m" + message + "\033[0m")

