print("Introduzca una contraseña.\n")

A = input("Introduzca su contraseña: ")
A = A.lower() #Comando para reducir todas la letras a minusculas
print(A)
if A == "contraseña":
    print("Contrasena correcta.")
else:
    print("Contrasena incorrecta.")

print("\nGracias por usar el programa.")