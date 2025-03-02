class Enteros:
    
    def __init__(self, n):
        self.n = n
        
        
    def print_numbers(self):
       for number in range(self.n):
           if((self.n%2)==0):
               print("El numero ingresado es: ",number)
           else:
               print("El cuadrado del numero es: ", number**2)

        
print("Mauricio Yael Pasten Jardon")
print("Ingresa un numero entero: ")
num = int(input()) 
enteros = Enteros(num)            
enteros.print_numbers()