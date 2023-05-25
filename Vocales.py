#Hacer un programa que pida un caracter e indicar si es una vocal o no.

letra = input("Teclea una letra: ").lower() #El lower sirve para crear una copia de la letra y la convierte en minúscula

if letra=='a' or letra=='e' or letra=='i' or letra=='o' or letra=='u':
    print("Es una vocal")
else:
    print("No es una vocal")

#Carolina EM