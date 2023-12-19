﻿import time
from colorama import init
from termcolor import colored

init()

def slow_print(text, delay=0.01):
    
    for char in text:
        
        print(char, end='', flush=True)
        time.sleep(delay)
        
    print()

class Menu:
    lista_de_meniuri = []

    def __init__(self,name:str,logo:str):
        self.name = name
        self.logo = logo
        Menu.lista_de_meniuri.append(self)

    def GetMenuByName (name:str):
        for menu in Menu.lista_de_meniuri:
            if menu.name == name:
                return menu
        ##
        raise Exception("Nu exista un meniu cu asa nume!")

    def InitAllMenues():
        MainMenuLogo = colored('''
        
    ██████╗░██████╗░░█████╗░░░░░░██╗███████╗░█████╗░████████╗  
    ██╔══██╗██╔══██╗██╔══██╗░░░░░██║██╔════╝██╔══██╗╚══██╔══╝  
    ██████╔╝██████╔╝██║░░██║░░░░░██║█████╗░░██║░░╚═╝░░░██║░░░  
    ██╔═══╝░██╔══██╗██║░░██║██╗░░██║██╔══╝░░██║░░██╗░░░██║░░░  
    ██║░░░░░██║░░██║╚█████╔╝╚█████╔╝███████╗╚█████╔╝░░░██║░░░  
    ╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░╚════╝░╚══════╝░╚════╝░░░░╚═╝░░░  -v1.0

    ███╗░░░███╗░█████╗░███╗░░██╗░█████╗░░██████╗░███████╗██████╗░
    ████╗░████║██╔══██╗████╗░██║██╔══██╗██╔════╝░██╔════╝██╔══██╗
    ██╔████╔██║███████║██╔██╗██║███████║██║░░██╗░█████╗░░██████╔╝
    ██║╚██╔╝██║██╔══██║██║╚████║██╔══██║██║░░╚██╗██╔══╝░░██╔══██╗
    ██║░╚═╝░██║██║░░██║██║░╚███║██║░░██║╚██████╔╝███████╗██║░░██║
    ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝░╚═════╝░╚══════╝╚═╝░░╚═╝
        ''','blue')
        menu1 = Menu("MainMenu",MainMenuLogo)
        ##
        HelpMenuLogo = colored('''
        
        ██╗░░██╗███████╗██╗░░░░░██████╗░
        ██║░░██║██╔════╝██║░░░░░██╔══██╗
        ███████║█████╗░░██║░░░░░██████╔╝
        ██╔══██║██╔══╝░░██║░░░░░██╔═══╝░
        ██║░░██║███████╗███████╗██║░░░░░
        ╚═╝░░╚═╝╚══════╝╚══════╝╚═╝░░░░░

        ░██████╗███████╗░█████╗░████████╗██╗░█████╗░███╗░░██╗
        ██╔════╝██╔════╝██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║
        ╚█████╗░█████╗░░██║░░╚═╝░░░██║░░░██║██║░░██║██╔██╗██║
        ░╚═══██╗██╔══╝░░██║░░██╗░░░██║░░░██║██║░░██║██║╚████║
        ██████╔╝███████╗╚█████╔╝░░░██║░░░██║╚█████╔╝██║░╚███║
        ╚═════╝░╚══════╝░╚════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝

        
        ''','blue')
        menu2 = Menu("HelpMenu",HelpMenuLogo)
        ##
        AboutMenuLogo = colored('''

        ░█████╗░██████╗░░█████╗░██╗░░░██╗████████╗
        ██╔══██╗██╔══██╗██╔══██╗██║░░░██║╚══██╔══╝  
        ███████║██████╦╝██║░░██║██║░░░██║░░░██║░░░  
        ██╔══██║██╔══██╗██║░░██║██║░░░██║░░░██║░░░  
        ██║░░██║██████╦╝╚█████╔╝╚██████╔╝░░░██║░░░  
        ╚═╝░░╚═╝╚═════╝░░╚════╝░░╚═════╝░░░░╚═╝░░░  
        
        ░██████╗███████╗░█████╗░████████╗██╗░█████╗░███╗░░██╗
        ██╔════╝██╔════╝██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║
        ╚█████╗░█████╗░░██║░░╚═╝░░░██║░░░██║██║░░██║██╔██╗██║
        ░╚═══██╗██╔══╝░░██║░░██╗░░░██║░░░██║██║░░██║██║╚████║
        ██████╔╝███████╗╚█████╔╝░░░██║░░░██║╚█████╔╝██║░╚███║
        ╚═════╝░╚══════╝░╚════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝
        ''','blue')
        menu3 = Menu("AboutMenu",AboutMenuLogo)
        


