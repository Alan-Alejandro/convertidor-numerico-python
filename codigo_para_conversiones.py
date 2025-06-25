#este Programa es para la conversión de los distintos tipos de numeración a otros en python 


# Menú diccionario para elegir origen y destino 
sistemas = { 
    "1": "Decimal",
    "2": "Binario",
    "3": "Octal",
    "4": "Hexadecimal"
}
def mostrar_sistemas():  # se crea o define una fucnion que podra ser reutilizada infinitasveces
    print("Sistemas de numeración disponibles:")
    for clave, valor in sistemas.items(): #con un bucle for se recorre el diccionario sistemas, y en cada vuelta crea dos variables temporales: clave y valor.
# .items() convierte el diccionario en pares clave:valor (como tuplas)x
        print(f"{clave}. {valor}") #llamo a los valores creados de la variable mostrar_sistemas con el f string.


while True:
    print("\n--- Convertidor de Sistemas Numéricos ---")
    mostrar_sistemas()
    
    origen = input("Selecciona el sistema de origen (1-4): ")
    destino = input("Selecciona el sistema de destino (1-4): ")
    
    if origen == destino:
     print("\nEl sistema de origen y destino no puede ser el mismo.")

    
    elif origen not in sistemas or destino not in sistemas:
     print("Selección inválida. Intenta de nuevo.")
     continue


    numero = input(f"Ingrese el número en formato {sistemas[origen]}: ") # {sistemas[origen]}: llama al diccionario 



 # siguiente paso de la conversion creo las funciones y las emparejo con sus casos de uso 

#  podira hacer 12 fucniones convertidoras pero mejor hare un convertidor general que convierta todo a decimal primero y de ahí al sistema deseado ya que es más eficiente.
# como resultado hare 6 funciones en total en lugar de 12 iual como se hace en matematicas ya que es mas sencillo

     
    def binario_a_decimal(numero):
       try:
          return int(numero, 2)  # intenta convertirlo desde binario a decimal
       except ValueError:
          return "Número binario inválido"
         
    def decimal_a_binario(numero):
        try:
           numero_entero = int(numero)  # Asegura que sea número decimal válido 
           return bin(numero_entero)[2:]  # Convierte a binario y elimina el prefijo '0b' del inicio
        except ValueError:
          return "Número decimal inválido"
        
    def decimal_a_octal(numero):
        try:
            numero_entero = int(numero)
            return oct(numero_entero)[2:]
        except ValueError:
            return "numero decimal invalido" 
        
    def octal_a_decimal (numero):
        try:
            return int(numero, 8)
        except ValueError:
            return "numero octal invalido"
        
    def hexadecimal_a_decimal(numero):
        try:
            return int(numero, 16)
        except ValueError:
            return "numero hexadecimal invalido"
           
    def decimal_a_hexadecimal(numero):
        try:
            numero_entero = int(numero)
            return hex(numero_entero)[2:]
        except ValueError:
            return "numero hexadecimal invalido"

#aqui convierto primero los numeros a decimal para luego convertirlos en lo que se dese ya que de esta manera ahorro mucho codigo
    if origen == destino :
       resultado = numero #no convierto ya que es igual.

    elif sistemas [origen] == "Binario":
      decimal = binario_a_decimal(numero)

    elif sistemas [origen] == "Octal" :
      decimal = octal_a_decimal(numero) 

    elif sistemas [origen] == "Hexadecimal":
      decimal = hexadecimal_a_decimal(numero)
    else:
       decimal = numero

    if sistemas[destino] == "Decimal":
        resultado = decimal

    elif sistemas[destino] == "Binario":
        resultado = decimal_a_binario(decimal)

    elif sistemas[destino] == "Octal":
        resultado = decimal_a_octal(decimal)
    
    elif sistemas[destino] == "Hexadecimal" :           
        resultado = decimal_a_hexadecimal(decimal)


    print(f"\nConvertiremos {numero} de {sistemas[origen]} a {sistemas[destino]} : {resultado}")
    
    otra = input("¿Deseas hacer otra conversión? (s/n): ").lower() #pregutna si desdea hacer mas conversiones, .lower se asegura de que sea minuscula para no meter doble codigo con S mayuscula 
    if otra != "s": 
     print (f"¡Hasta luego!"
            "\n-sal a tocar pasto"
            )
     break
    else : 
       continue

