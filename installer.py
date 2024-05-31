from colorama import init, Fore
import os
import subprocess

GREEN = '\033[92m'
CYAN  = '\033[96m'
WHITE = '\033[97m'
RED = '\033[91m'
BLUE = '\033[94m'
END = '\033[0m'

def banner_installer():
    print(Fore.RED + "▄▄▄▄·  ▄ .▄▄ •▄     ▪   ▐ ▄ .▄▄ ·▄▄▄▄▄ ▄▄▄· ▄▄▌  ▄▄▌  ▄▄▄ .▄▄▄  ")
    print(Fore.RED + "▐█ ▀█▪██▪▐██▌▄▌▪    ██ •█▌▐█▐█ ▀.•██  ▐█ ▀█ ██•  ██•  ▀▄.▀·▀▄ █·")
    print(Fore.RED + "▐█▀▀█▄██▀▐█▐▀▀▄·    ▐█·▐█▐▐▌▄▀▀▀█▄▐█.▪▄█▀▀█ ██▪  ██▪  ▐▀▀▪▄▐▀▀▄ ")  
    print(Fore.RED + "██▄▪▐███▌▐▀▐█.█▌    ▐█▌██▐█▌▐█▄▪▐█▐█▌·▐█ ▪▐▌▐█▌▐▌▐█▌▐▌▐█▄▄▌▐█•█▌")
    print(Fore.RED + "·▀▀▀▀ ▀▀▀ ··▀  ▀    ▀▀▀▀▀ █▪ ▀▀▀▀ ▀▀▀  ▀  ▀ .▀▀▀ .▀▀▀  ▀▀▀ .▀  ▀")

def menu():
    print(Fore.GREEN + "Selecciona una opcion")
    print(Fore.GREEN + "1.-", Fore.CYAN + "Instalar en linux (solo derivaciones de debian)")
    print(Fore.GREEN + "2.-", Fore.CYAN + "Instalar en termux")
    print(Fore.GREEN + "00.-", Fore.CYAN + "exit")


def kali_install():
    def banner_kali():
        print(Fore.RED + "▄▄▄▄·  ▄ .▄▄ •▄     ▪   ▐ ▄ .▄▄ · ▄▄▄▄▄ ▄▄▄· ▄▄▌  ▄▄▌  ▄▄▄ .▄▄▄  ")
        print(Fore.RED + "▐█ ▀█▪██▪▐██▌▄▌▪    ██ •█▌▐█▐█ ▀. •██  ▐█ ▀█ ██•  ██•  ▀▄.▀·▀▄ █·")
        print(Fore.RED + "▐█▀▀█▄██▀▐█▐▀▀▄·    ▐█·▐█▐▐▌▄▀▀▀█▄ ▐█.▪▄█▀▀█ ██▪  ██▪  ▐▀▀▪▄▐▀▀▄ ")
        print(Fore.RED + "██▄▪▐███▌▐▀▐█.█▌    ▐█▌██▐█▌▐█▄▪▐█ ▐█▌·▐█ ▪▐▌▐█▌▐▌▐█▌▐▌▐█▄▄▌▐█•█▌")
        print(Fore.RED + "·▀▀▀▀ ▀▀▀ ··▀  ▀    ▀▀▀▀▀ █▪ ▀▀▀▀  ▀▀▀  ▀  ▀ .▀▀▀ .▀▀▀  ▀▀▀ .▀  ▀")
        print(Fore.RED + "                ▪   ▐ ▄     ▄ •▄  ▄▄▄· ▄▄▌  ▪                    ")
        print(Fore.RED + "                ██ •█▌▐█    █▌▄▌▪▐█ ▀█ ██•  ██                   ")
        print(Fore.RED + "                ▐█·▐█▐▐▌    ▐▀▀▄·▄█▀▀█ ██▪  ▐█·                  ")
        print(Fore.RED + "                ▐█▌██▐█▌    ▐█.█▌▐█ ▪▐▌▐█▌▐▌▐█▌                  ")
        print(Fore.RED + "                ▀▀▀▀▀ █▪    ·▀  ▀ ▀  ▀ .▀▀▀ ▀▀▀                  ")

    def menu_kali():
        os.system('clear')
        print("\033[92mSelecciona una opción:")
        print("\033[92m1. \033[96mInstalar dependencias y las herramientas")
        print("\033[92m00. \033[96mSalir")

    def instalar_en_kali():
        print("\033[92mInstalando en kali linux...")

        # Instalando las dependencias
        os.system("pip install pyngrok requests wget pyshorteners")
        subprocess.run(['sudo', 'apt', 'install', '-y', 'megatools', 'unzip', 'wget', 'curl', 'php'])

        # Instalando la herramienta
        print("\033[92mInstalando la herramienta, espere un poco...")
        subprocess.run(['megatools', 'dl', 'https://mega.nz/file/yAwGSKLA#CXVvFBqkk15GHEpTN8APqNX2eEs6oSxDMI1IfnnJkPY'])
        subprocess.run(['unzip', 'Black-Hack-Kit.zip'])
        os.remove('Black-Hack-Kit.zip')
        os.system(f"cd Black-Hack-Kit")
        subprocess.run(['python3', 'BHK.py'])

    banner_kali()
    menu_kali()

    opcion = input("Ingresa el número de la opción: ")

    if opcion == '1':
        instalar_en_kali()
    elif opcion == '00':
        print("Saliendo...")
        os.system(f"exit")
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")


def termux_install():
    def banner_termux():
        print(Fore.RED + "▄▄▄▄·  ▄ .▄▄ •▄     ▪   ▐ ▄ .▄▄ · ▄▄▄▄▄ ▄▄▄· ▄▄▌  ▄▄▌  ▄▄▄ .▄▄▄  ")
        print(Fore.RED + "▐█ ▀█▪██▪▐██▌▄▌▪    ██ •█▌▐█▐█ ▀. •██  ▐█ ▀█ ██•  ██•  ▀▄.▀·▀▄ █·")
        print(Fore.RED + "▐█▀▀█▄██▀▐█▐▀▀▄·    ▐█·▐█▐▐▌▄▀▀▀█▄ ▐█.▪▄█▀▀█ ██▪  ██▪  ▐▀▀▪▄▐▀▀▄ ")
        print(Fore.RED + "██▄▪▐███▌▐▀▐█.█▌    ▐█▌██▐█▌▐█▄▪▐█ ▐█▌·▐█ ▪▐▌▐█▌▐▌▐█▌▐▌▐█▄▄▌▐█•█▌")
        print(Fore.RED + "·▀▀▀▀ ▀▀▀ ··▀  ▀    ▀▀▀▀▀ █▪ ▀▀▀▀  ▀▀▀  ▀  ▀ .▀▀▀ .▀▀▀  ▀▀▀ .▀  ▀")
        print(Fore.RED + "        ▪   ▐ ▄     ▄▄▄▄▄▄▄▄ .▄▄▄  • ▌ ▄ ·. ▄• ▄▌▐▄• ▄           ")
        print(Fore.RED + "        ██  •█▌▐█    •██  ▀▄.▀·▀▄ █··██ ▐███▪█▪██▌ █▌█▌▪          ")
        print(Fore.RED + "        ▐█ ·▐█▐▐▌     ▐█.▪▐▀▀▪▄▐▀▀▄ ▐█ ▌▐▌▐█·█▌▐█▌ ·██·           ")
        print(Fore.RED + "        ▐█▌ ██▐█▌     ▐█▌·▐█▄▄▌▐█•█▌██ ██▌▐█▌▐█▄█▌▪▐█·█▌          ")
        print(Fore.RED + "        ▀▀▀ ▀▀ █▪     ▀▀▀  ▀▀▀ .▀  ▀▀▀  █▪▀▀▀ ▀▀▀ •▀▀ ▀▀          ")

    def menu_termux():
        os.system('clear')
        print("\033[92mSelecciona una opción:")
        print("\033[92m1. \033[96mInstalar Dependencias")
        print("\033[92m2. \033[96mInstalar La herramienta")
        print("\033[92m00. \033[96mSalir")

    def instalar_en_termux():
        print("\033[92mInstalando en termux...")
        subprocess.run("pip install pyngrok requests wget pyshorteners")

        subprocess.run(['apt', 'install', '-y', 'megatools', 'unzip'])
        print("\033[92mInstalando la herramienta, espere un poco...")
        subprocess.run(['megatools', 'dl', 'https://mega.nz/file/yAwGSKLA#CXVvFBqkk15GHEpTN8APqNX2eEs6oSxDMI1IfnnJkPY'])
        subprocess.run(['unzip', 'Black-Hack-Kit.zip'])
        os.remove('Black-Hack-Kit.zip')
        os.chdir('Black-Hack-Kit')
        subprocess.run(['python3', 'index.py'])

    banner()
    mostrar_menu()

    opcion = input("Ingresa el número de la opción: ")

    if opcion == '1':
        instalar_dependencias()
    elif opcion == '2':
        instalar_herramienta()
    elif opcion == '00':
        print("Saliendo...")
        os.system(f"exit")
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")

banner_installer()
menu()
system = input("Ingresa el número de la opción: ")

if system == "1":
    kali_install()
elif system == "2":
    termux_install()
else:
    os.system(f"exit")