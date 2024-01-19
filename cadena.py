cadena = input("Ingrese el numero que desea invertir:  ")
invertir = ""
for i in range(len(cadena)):
    invertir += cadena[-(i+1)]
print(invertir)
