#Calculadora de operaciones basicas

def suma(a,b):
    summa = a+b
    return summa

def resta(a,b):
    ressta = a-b
    return ressta

def multiplicacion(a,b):
    mulltiplicacion = a*b
    return mulltiplicacion

def division(a,b):
    divvision = a/b
    return divvision

def menu():
    
    print("---------------------MENU PRINCIPAL---------------------")
    print("1.Suma")
    print("2.Resta")
    print("3.Multiplicacion")
    print("4.Division")
    
    elegir_opcion = int(input("Ingresar la operacion que desea: "))
    numero1 = int(input("Ingresar el primer numero: "))
    numero2 = int(input("Ingresar el segundo numero: "))
    
    if elegir_opcion==1:
        print("La suma es:", suma(numero1,numero2))
    elif elegir_opcion==2:
        print("La resta es: ", resta(numero1,numero2))
    elif elegir_opcion==3:
        print("La multiplicacion es: ", multiplicacion(numero1,numero2))
    elif elegir_opcion == 4:
        print("La division es: ", division(numero1,numero2))
    else:
        print("No existe esta operacion")
    return menu
menu()
