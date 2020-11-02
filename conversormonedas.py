menu = """
BIENVENIDO AL CONVERSOR DE MONEDAS
1.- PESOS COLOMBIANOS
2.- PESOS ARGENTINOS
3.- PESOS MEXICANOS
ELIGE UNA OPCION: """
opcion = int(input(menu))
if opcion == 1:
    pesos = input("Cuantos pesos colombianos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 3875
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tiene $"+ dolares +"dolares")
elif opcion == 2:
    pesos = input("Cuantos pesos argentino tienes?: ")
    pesos = float(pesos)
    valor_dolar = 3875
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tiene $"+ dolares +"dolares")
elif opcion == 3:
    pesos = input("Cuantos pesos mexicano tienes?: ")
    pesos = float(pesos)
    valor_dolar = 3875
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tiene $"+ dolares +"dolares")
else:
    print('Ingresa una opcion correcta por favor')



