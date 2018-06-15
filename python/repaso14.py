cuenta = 0
suma = 0
for i in range(1, 10):
    if (i % 2) == 1:
        cuenta = cuenta + 1
        suma = suma + i

print ("Hay" + str(cuenta) +"numeros impares")
print("la suma es " + str(suma))