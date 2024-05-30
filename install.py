import os
import subprocess

def mostrar_menu():
    os.system('clear')
    print("\033[92mSelecciona una opción:")
    print("\033[92m1. \033[96mInstalar La herramienta y sus dependencias")
    print("\033[92m00. \033[96mSalir")


def instalar_herramienta():
    print("\033[92mInstalando la herramienta y sus dependencias, espere un poco...")
    subprocess.run(['apt', 'install', 'megatools', 'apt', 'install', 'unzip', '-y', '&&', 'pip install colorama'])

    os.system(f"megadl https://mega.nz/file/nIxSjCiC#-jZqXATBU2lxAcADyN6QVEXHcaqC8oWz0S8AOJG0vhY")

    os.system(f"unzip Black-Hack-Kit.zip")

    os.remove('Black-Hack-Kit.zip')

    os.chdir("cd Black-Hack-Kit")

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
