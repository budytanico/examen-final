# Programa condicion multiple

marca = input ("Escribe la marca de la tarjeta gráfica")
modelo = input ("Escribe modelo ")

precio = 1000

if marca == "MSI" or marca =="msi" or marca == "Msi":
    descuento = 5;

if marca == "MSI" or marca =="GTX" or marca == "gtx":
    descuento = 10;

if marca == "MSI" or marca =="IT" or marca == "it":
    descuento = 20;

precio = precio - (precio * (descuento/100))
print (' El precio final es ' + str(precio) + '€')
