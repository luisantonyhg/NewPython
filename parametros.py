
def resta(a,b):
    return a - b

print(resta(5,2))

def suma(e,s):
    return e + s

print(suma(10,3))

# HACIENDO UNA FUNCION CON IF Y ELSE

def multiplicar(a=None,b=None):
    if a == None or b == None:
        print("Error, enviar dos numeros a la funcion")
        return
    else:
        return a+b

print(multiplicar(2,2))


# HACIENDO UNA FUNCION CON ARGUMENTO O PARAMETRO CON VALOR

def duplicar(numero):
    return numero*2
n=15

print(duplicar(n),n)