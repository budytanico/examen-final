def saludar(nombre, mensaje=' Buenos dias wey '):
    print (mensaje + nombre)

usuario = input ("Introduce nombre")
saludar(usuario)

def edad(edad, mensaje=' Pareces má joven que '):
    print (mensaje + str(edad))

anyos = int(input ("Introduce edad"))
edad(anyos)

