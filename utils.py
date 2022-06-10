import os


def clear_stdout():
    os.system("cls" if os.name == "nt" else "clear")
