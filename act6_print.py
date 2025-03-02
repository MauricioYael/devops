print("Hola Mauricio, ingresa un numero entero")

try:
    n = int(input())
    print("el numero ingresado es:", n)

    for number in range(n):
        print(number)
except:
    print ("La entrada no es entero")