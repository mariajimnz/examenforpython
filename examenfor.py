multiplos_2 = 0
multiplos_3 = 0
add_num = True
while add_num:
    numero = int(input("Ingrese un número: "))
    if numero % 2 == 0:
        multiplos_2 += 1
    elif numero % 3 == 0:
        multiplos_3 += 1
    otro_num = input("¿Agregar otro número? S/N ").upper()
    if otro_num == "N":
        print(f"Hay {multiplos_2} multiplos de 2 y {multiplos_3} multiplos de 3")
        add_num = False
    elif otro_num == "S":
        continue


frutas_agregadas = []
cantidad_frutas = 10
for x in range(10):
    agregar_frutas = input(f"Añada {cantidad_frutas} frutas al salpicón: ")
    cantidad_frutas -= 1
    frutas_agregadas.insert(0, agregar_frutas)

print(frutas_agregadas)

from random import randint
print("Bienvenido al menú automatico.")
cinco_enteros = [str(randint(1, 100)) for x in range(5)]

while True:
    numero_digitado = input("Presione 1 para recibir 5 números enteros, "
                            "presione 2 para sumarlos, presione 3 para añadir mas números y 4 para salir del menú: ")

    if numero_digitado == "1":
        print(", ".join(cinco_enteros))
    elif numero_digitado == "2":
        sumar_enteros = [int(x) for x in cinco_enteros]
        print(sum(sumar_enteros))
    elif numero_digitado == "3":
        nuevo_numero = input("Añade otro número: ")
        cinco_enteros.append(nuevo_numero)
    elif numero_digitado == "4":
        print("¡Hasta luego!")
        break















