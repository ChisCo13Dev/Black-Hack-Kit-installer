import os
import subprocess

def mostrar_menu():
    os.system('clear')
    print("\033[92mSelecciona una opción:")
    print("\033[92m1. \033[96mInstalar Dependencias")
    print("\033[92m2. \033[96mInstalar La herramienta")
    print("\033[92m00. \033[96mSalir")

def instalar_dependencias():
    print("\033[92mInstalando Megatools...")
    subprocess.run(['apt', 'install', 'megatools', '-y'])
    print("\033[92mInstalando unzip...")
    subprocess.run(['apt', 'install', 'unzip', '-y'])

def instalar_herramienta():
    print("\033[92mInstalando la herramienta, espere un poco...")
    os.system(f"megadl https://mega.nz/file/nIxSjCiC#-jZqXATBU2lxAcADyN6QVEXHcaqC8oWz0S8AOJG0vhY")

    os.system(f"unzip Black-Hack-Kit.zip")

    os.remove('Black-Hack-Kit.zip')

    os.chdir(f"cd Black-Hack-Kit")

    os.system(f"python3 index.py")

while True:
    mostrar_menu()

    opcion = input("Ingresa el número de la opción: ")

    if opcion == '1':
        instalar_dependencias()
    elif opcion == '2':
        instalar_herramienta()
    elif opcion == '00':
        print("Saliendo...")
        break
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")
