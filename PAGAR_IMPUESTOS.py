print("Sabe si usted debe tributar?\n")

nombre = input("Nombre: ")
edad = int(input("Edad: "))
ingresos = float(input("Ingresos mensuales aproximados: "))

if edad >= 16 and ingresos >= 1000:
    impuesto = ingresos * 0.02
    print("Apreciad@ ", nombre, ", usted debe pagar al estado la suma de: ", impuesto, " Gracias.")
else:
    print("Apreciad@ ", nombre, "Usted no califica para tributar. Gracias.")
