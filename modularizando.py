def conversor(tipo_pesos, valor_dolar):
    pesos = input("Cuantos pesos " + tipo_pesos + " tiene?:")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("tienes $" + dolares + "dolares")
    

menu = """
Bienvenido al conversor de monedas
1.- Pesos Colombianos
2.- Pesos Argetinos
3.- Pesos Mexicanos
Elige una opcion: """

opcion = int(input(menu))

if opcion == 1:
    conversor("colombianos", 3875)
elif opcion == 2:
    conversor("argetino", 65)
elif opcion == 3:
    conversor("mexicano", 24)
else:
    print('ingresa una opcion correcto')