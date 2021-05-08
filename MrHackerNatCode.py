#!/usr/bin/python3
# Created By : Mr.Hacker
from os import system, name
from time import sleep
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
clear()
from colorama import Fore
print(Fore.GREEN + """

███╗░░░███╗██████╗░  ░░░  ██╗░░██╗░█████╗░░█████╗░██╗░░██╗███████╗██████╗░
████╗░████║██╔══██╗  ░░░  ██║░░██║██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗
██╔████╔██║██████╔╝  ░░░  ███████║███████║██║░░╚═╝█████═╝░█████╗░░██████╔╝
██║╚██╔╝██║██╔══██╗  ░░░  ██╔══██║██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
██║░╚═╝░██║██║░░██║  ██╗  ██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗██║░░██║
╚═╝░░░░░╚═╝╚═╝░░╚═╝  ╚═╝  ╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
""")
print(Fore.YELLOW + """
1.Generate National Code ( For IRAN )
2.Connect With Me
3.Exit
""")
try :
    mrhacker = int(input(Fore.GREEN + "[+] " + Fore.BLUE + "Select A Number: "))
    if mrhacker == 1 :
        hacker = "250417855"
        while True :
            hacker = int(hacker) + int(1)
            print("0" + str(hacker))
    elif mrhacker == 2 :
        print(Fore.WHITE +   "Github    : github.com/MrHackerMr")
        print(Fore.RED   +   "Telegram  : @MrHackerMr")
        print(Fore.GREEN +   "Instagram : MrHackerMr")
    elif mrhacker == 3 :
        from os import system
        system("exit")
except ValueError :
    print(Fore.RED + "\n[+] " + Fore.BLUE + "OK, Have A Nice Life :) ")
# Created By : Mr.Hacker
