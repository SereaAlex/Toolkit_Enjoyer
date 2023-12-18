from menu_item import menu_item
from Menu import Menu
from colorama import init
import readline
import glob
from Functionality import Functions, Options

def custom_completer(text, state):
    matches = glob.glob(text + '*')
    return (matches + [None])[state]

readline.set_completer(custom_completer)
readline.parse_and_bind("tab: complete")

init()


Functions.clear_screen()
Menu.InitAllMenues()
Functions.InitHelpItems()
Functions.InitMenuItems()
Functions.PrintMenu("MainMenu")

while True:
    user_input = input("Type: ")
    menu_item.TryExec(user_input)
