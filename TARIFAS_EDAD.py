print("Tarifas del parque.\n")

nombre = input("Como te llamas? ")
edad = int(input("Que edad tienes? "))

if edad < 4:
    print ("Entras gratis. ")

elif edad < 18:
    print ("Debes pagar $5. ")

else:
    print("Debes pagar $10. ")

print("Gracias.")