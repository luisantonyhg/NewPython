def conversacion(mensaje):
    print('Hola')
    print('Como estas?')
    print(mensaje)
    print('Adios')

opcion = int(input('Elige una opcion (1,2,3):'))
if opcion == 1:
    conversacion('ELegiste la opcion 1')
elif opcion == 2:
    conversacion('Elegiste la opcion 2')
elif opcion == 3:
    conversacion('Elegiste la opcion 3')
else:
    print('Escribe la opcion correcta') 
def saludar():
    print("Hola, esto son las tablas de la multiplicacion")

saludar()

# # HACIENDO LA TABLA DE MULTIPLICACION CON FUNCIONES Y FOR

def tabla_del_5():
    for i in range(5):
        print(f"5 *  {i} = {5*i}")

tabla_del_5()

def tabla_del_6():
    for i in range(5):
        print(f"6 * {i} = {6*i}")
tabla_del_6()

def tabla_del_7():
    for i in range(5):
        print(f"7* {i} = {7*i}")
tabla_del_7()

def tabla_del_8():
    for i in range(5):
        print(f"8*{i} = {8*i}")

tabla_del_8()

def table_del_9():
    for i in range(5):
        print(f"9*{i} = {9*i}")

table_del_9()

def table_del_10():
    for i in range(5):
        print(f"10*{1} = {10*1}")

table_del_10()

# # EJERCICIOS DE FUNCIONES CON PRINT

def prueba():
    a=10
    print(a)
prueba()

def test():
    print(m)
m=8

test()

def testi():
     o = 5
     print(o)

testi()

# RETORNANDO VALORES CON FUNCIONES

def funcion():
    return "Este testo esta imprimido con return"

print(funcion())

def funcion1():
    return [1,2,3,4,5]

print(funcion1())

def funcional():
    return "Mensaje numero 1", 1994,[1,2,3]

print(funcional())

def funcionel():
    return "mensaje de python"

print(funcionel())



    

    