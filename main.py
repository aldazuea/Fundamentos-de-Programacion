# Arreglo Multibidimencional
a = [[15, 11, 17],[23, 25, 19],[13, 27, 29]]
#a.sort()
for x in range(len(a)):
    a[x]=sorted(a[x])
print (a)

numero = int(input("Ingresa un numero: "))

for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == numero:
                print (f"El número {numero} se encuentra en la fila {[i]}  y en la columna {[j]}")
