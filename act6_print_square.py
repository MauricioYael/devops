print("Mauricio Yael Pasten Jardon")
print("Ingresa un numero entero: ")
try:
    n = int(input())
    print("El numero ingresado es: " ,n)
    
    for number in range(n):
        if((n%2)==0):
            print("El numero ingresado es: ",number)
        else:
            print("El cuadrado del numero es: ", number**2)
except:
        print ("La entrada no es entero")