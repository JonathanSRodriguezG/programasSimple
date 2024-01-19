radio = float(input("Ingrese el radio del circulo: "))
import math
perimetro = 2*math.pi*radio
area = math.pi*(radio)**2
print(f"El perimetro del circulo con radio {radio} es: {perimetro}")
print(f"El area del circulo con radio {radio} es: {area}")