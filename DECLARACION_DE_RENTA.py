print("Descubra su TIPO IMPOSITIVO y su declaracion de renta.\n")

nombre = input("Nombre: ")
edad = int(input("Edad: "))
ingreso = int(input("Ingrese su renta anual: "))

if edad > 18:

    if ingreso < 10000:
        impuesto1 = ingreso * 0.05
        print("Apreciad@ ", nombre, ", su TIPO IMPOSITIVO es del 5%, debe pagar ", impuesto1, " Gracias.")
    
    elif ingreso < 20000:
        impuesto2 = ingreso * 0.15
        print("Apreciad@ ", nombre, ", su TIPO IMPOSITIVO es del 15%, debe pagar ", impuesto2, " Gracias.")

    elif ingreso < 35000:
        impuesto3 = ingreso * 0.2
        print("Apreciad@ ", nombre, ", su TIPO IMPOSITIVO es del 20%, debe pagar ", impuesto3, " Gracias.")

    elif ingreso < 60000:
        impuesto4 = ingreso * 0.3
        print("Apreciad@ ", nombre, ", su TIPO IMPOSITIVO es del 30%, debe pagar ", impuesto4, " Gracias.")

    else:
        impuesto5 = ingreso * 0.45
        print("Apreciad@ ", nombre, ", su TIPO IMPOSITIVO es del 45%, debe pagar ", impuesto5, " Gracias.")

else:
    print("No tiene edad suficiente para tributar con el estado.")

print("\nGracias.")