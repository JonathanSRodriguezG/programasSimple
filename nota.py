nota1 = float(input("Ingrese la primera nota del certamen:   "))
nota2 = float(input("Ingrese la segunda nota del certamen:   "))
notalab = float(input("Ingrese la tercera nota del lab:   "))
lab = notalab * 0.3
notatotalcertamenes = (60 - lab) / 0.7
nota3 = 3*notatotalcertamenes - nota1 - nota2
print(f"La nota que necesitas para aprobar es de : {nota3}")