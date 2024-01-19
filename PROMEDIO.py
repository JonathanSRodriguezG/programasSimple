notas = []
n = int(input("Ingrese la cantidad de notas: "))
for i in range(n):
    notas.append(float(input(f"Ingrese la nota {i+1}: ")))

sum = 0
for i in range(len(notas)):
    sum += notas[i]

print(f"Las notas {notas}")
print(f"El promedio es: {sum/len(notas)}")