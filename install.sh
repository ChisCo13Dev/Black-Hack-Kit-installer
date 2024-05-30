#!/bin/bash

GREEN='\033[92m'
CYAN='\033[96m'
WHITE='\033[97m'
RED='\033[91m'
BLUE='\033[94m'
END='\033[0m'

mostrar_menu() {
    clear
    echo -e "${GREEN}Selecciona una opción:"
    echo -e "${GREEN}1. ${CYAN}Instalar Dependencias"
    echo -e "${GREEN}2. ${CYAN}Instalar La herramienta"
    echo -e "${GREEN}00. ${CYAN}Salir"
}

instalar_dependencias() {
    echo "${GREEN}Instalando Megatools..."
    apt install megatools -y  
    echo -e "${GREEN}Instalando unzip"
    apt install unzip
}

instalar_herramienta() {
    echo -e "${GREEN}Instalando la herramienta espere un poco..."
    megadl https://mega.nz/file/nIxSjCiC#-jZqXATBU2lxAcADyN6QVEXHcaqC8oWz0S8AOJG0vhY
    unzip 'Black Hack Kit.zip'
    rm -rf 'Black Hack Kit.zip'
    cd 'Black Hack Kit'
    python3 index.py
}

while true; do
    mostrar_menu

    read -p "Ingresa el número de la opción: " opcion

    case $opcion in
        1)
            instalar_dependencias
            ;;
        2)
            instalar_herramienta
            ;;
        00)
            echo "Saliendo..."
            break
            ;;
        *)
            echo "Opción inválida. Por favor, selecciona una opción válida."
            ;;
    esac
done
