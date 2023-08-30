def ingresaNumeros ():
    global n1, n2
    n1 = int(input("Ingresa el primer numero: "))
    n2 = int(input("Ingresa el segundo nunero: "))
    
    def sumar (a,b):
        print("El resultado de ",a," + ",b," = ",a+b)
        
    def restar (a,b):
        print("El resultado de ",a," - ",b," = ",a-b)
        
    def multiplicar (a,b):
        print("El resultado de ",a," x ",b," = ",a*b)
        
    def dividir (a,b):
        if b==0:
            print("No se puede hacer la división entre 0")
        else:
            print("El resultado de ",a," / ",b," = ",a/b)
        
            
print("Selecciona la operación a realizar: ")

opcion = int(input())


if opcion == 1:
    ingresaNumeros()
    sumar(n1, n2)
    
elif opcion ==2:
    ingresaNumeros()
    restar(n1, n2)
    
elif opcion ==3:
    ingresaNumeros()
    multiplicar(n1, n2)
    
elif opcion ==4:
    ingresaNumeros()
    dividir(n1, n2)
    
elif opcion ==5:
    print("Adios")

    
    
    