from figuras_geometricas import Figuras_geometricas
from triangulo import Triangulo
from cuadrado import cuadrado
from circulo import Circulo
from rectangulo import rectangulo
from cilindro import Cilindro
from paralelograma import Paralelograma
from pentágono import Pentagono
from trapecio import Trapecio


while True :
    print("------------------------------------Menu de opciones-------------------------------")
    print ("opçion 1: cuadrado")
    print ("opcion 2: triangulo")
    print ("opcion 3: circulo")
    print ("opcion 4: rectangulo")
    print ("opcion 5: cilindro")
    print ("opcion 6: paralelograma") 
    print ("opcion 7: pentagono")
    print ("opcion 8: trapecio")
    print ("opcion 9: salir")
    opcion = input("ingrese la opcion deseada :")

    if opcion == "1" :
         lado = float(input("Digite el valor del lado del cuadrado: "))
         figura1 = cuadrado(lado)
         print("El área del cuadrado es:", figura1.area())

    if opcion =="2"  :

        base = float(input("Digite la base del triángulo: "))
        altura = float(input("Digite la altura del triángulo: "))
        figura2 = Triangulo(base, altura)
        print("El área del triángulo es:", figura2.area())

    if opcion == "3"  :
        radio = float(input("digite el radio del circulo: "))
        figura3 = Circulo(radio)
        print("El área del círculo es:", figura3.area())

    if opcion == "4"   :
        base = float(input("Digite la base del rectangulo: "))
        altura = float(input("Digite la altura del rectangulo: "))
        figura4 = rectangulo(base, altura)
        print("El área del triángulo es:", figura4.area())

    if opcion == "5":
        radio = float(input("Digite el radio del cilindro: "))
        altura = float(input("Digite la altura del cilindro: "))
        figura5 = Cilindro("Cilindro", radio, altura)
        print("El área del cilindro es:", figura5.area())

    if opcion == "6":
        base = float(input("Digite la base del paralelogramo: "))
        altura = float(input("Digite la altura del paralelogramo: "))
        figura6 = Paralelograma("Paralelograma", base, altura)
        print("El área del paralelogramo es:", figura6.area())

    if opcion == "7":
        lado = float(input("Digite el lado del pentágono: "))
        apotema = float(input("Digite la apotema del pentágono: "))
        figura7 = Pentagono("Pentágono", lado, apotema)
        print("El área del pentágono es:", figura7.area())

    if opcion == "8":
        base_mayor = float(input("Digite la base mayor del trapecio: "))
        base_menor = float(input("Digite la base menor del trapecio: "))
        altura = float(input("Digite la altura del trapecio: "))
        figura8 = Trapecio("Trapecio", base_mayor, base_menor, altura)
        print("El área del trapecio es:", figura8.area())

    elif opcion == "9":
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida, intenta de nuevo.")

nombre=input ("que figura desea usar")
print("la fugura seleccionada es: ", nombre)

#instancio clase padre figura geometrica
fg=Figuras_geometricas(nombre)
#llamo la funcion par calcular el area 
fg.area()
 