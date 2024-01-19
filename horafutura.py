horas = [1,24]
hora = float(input("Ingrese la hora actual:  "))
h = int(input("Cantidad de horas:  "))
futuro = (hora + h) %24
print(f"Dentro de {h} horas, el reloj marcará las {futuro}")