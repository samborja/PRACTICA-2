print("ERROR EN DIVISIÓN.\n")

print("Usted deverá introducir dos numero, numerados y denominador.\n")

A = int(input("Introduzca el primer número: "))
B = int(input("Introduzca el segundo número: "))

if B == 0:
    print("No sea tan bruto hpt. :)")
else:
    C = A / B
    print("El resultado de la división es: ", C)

print("\nGracias por usar el programa.")