edad = int(input("Escribe tu edad :"))
print(edad)

if edad > 17:
    print("eres mayor de edad")
else:
    print("No eres mayor de edad")

numero = int(input("Escribe un numero: "))

if numero > 5:
    print('es mayor a 5')
elif numero == 5:
    print('es igual a 5')
else:
    print('es menor a 5')


ventas_de_entradas = int(input("La entrada cuesta tanto: "))

if ventas_de_entradas < 20:
    print('Cuesta 10')

elif ventas_de_entradas == 20:
    print('es el mismo precio')

else:
    print('es el menor')


