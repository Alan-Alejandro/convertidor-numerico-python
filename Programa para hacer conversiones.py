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

    # siguiente paso de la conversion 
    print(f"\n-Convertiremos {numero} de {sistemas[origen]} a {sistemas[destino]}. (falta implementar)")
    
    otra = input("¿Deseas hacer otra conversión? (s/n): ").lower() #pregutna si desdea hacer mas conversiones, .lower se asegura de que sea minuscula para no meter doble codigo con S mayuscula 
    if otra != "s": 
     print (f"¡Hasta luego!"
            "\n-sal a tocar pasto"
            )
     break
    else : 
       continue
# hasta aqui es solo el menu de seleccion, falta crear las funciones encargadas de la conversion numerica que estan a continuacion.

# nueva fucnion, podira hacer 12 fucniones convertidoras pero mejor hare un convertidor general que convierta todo a decimal primero y de ahí al sistema deseado ya que es más eficiente.
# como resultado hare 6 funciones en total en lugar de 12 iual como se hace en matematicas ya que es mas sencillo jeje
def binario_a_decimal(numero):
   print
