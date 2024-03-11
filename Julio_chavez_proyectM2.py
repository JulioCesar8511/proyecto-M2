def determinar_cuadrante(x, y):
    if x == 0 or y == 0:
        print("Las coordenadas no pueden ser cero.")
        return
    
    if x > 0 and y > 0:
        print("El punto se encuentra en el cuadrante I.")
    elif x < 0 and y > 0:
        print("El punto se encuentra en el cuadrante II.")
    elif x < 0 and y < 0:
        print("El punto se encuentra en el cuadrante III.")
    else:
        print("El punto se encuentra en el cuadrante IV.")

def main():
    x = int(input("Ingrese X: "))
    y = int(input("Ingrese Y: "))
    determinar_cuadrante(x, y)

if __name__ == "__main__":
    main()
#Este programa solicita al usuario que ingrese dos números, 
# que representan las coordenadas X e Y respectivamente. 
# Luego, determina en qué cuadrante se encuentra el punto representado por esas coordenadas y muestra el resultado. 
# Además, verifica que ninguna de las coordenadas sea cero
