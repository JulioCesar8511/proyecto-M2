def verificar_longitud_palabra(palabra):
    longitud = len(palabra)
    if 4 <= longitud <= 8:
        print("La palabra es correcta.")
    elif longitud < 4:
        print(f"Hacen falta letras. Solo tiene {longitud} letras.")
    else:
        print(f"Sobran letras. Tiene {longitud} letras.")

def main():
    palabra = input("Ingrese una palabra: ")
    verificar_longitud_palabra(palabra)

if __name__ == "__main__":
    main()
#Este programa solicita al usuario que ingrese una palabra, luego verifica la longitud de la palabra ingresada 
# y proporciona un mensaje apropiado según las condiciones establecidas
