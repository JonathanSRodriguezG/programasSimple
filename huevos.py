To = float(input("Ingrese la temperatura inicial del huevo: ")) #temperatura inicial
tamañohuevo = input("Su huevo es A o AA ?:  ")
if tamañohuevo =="A":
    M=47
elif tamañohuevo =="AA":
    M=67
else: 
    print("Escriba un tamaño válido.")

p = 1.038
c = 3.7
k = 5.4 *10**-3
Ty = 70
Tw = 100
import math
t = ( (M**(2/3) * c * p**(1/3)) / (k * math.pi**2 * ((4 * math.pi)/3)**(2/3) ) * math.log( 0.76 * ((To - Tw)/(Ty - Tw)) ))
print(f"El tiempo que demora en alcanzar la temperatura máxima es: {round(t)} segundos")
print(f"El tiempo que demora en alcanzar la temperatura máxima es: {round(t/60)} minutos")


