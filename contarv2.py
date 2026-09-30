#contar de 1 a 10
nombre = input ("Hola, cual es tunombre:").upper()
contar=int(input(f" {nombre} hasta que numero quieres contar"))

if contar >10:
    print ("error, el numero debe ser menor que 10")


else:
    for num in range(contar):
        print(num+1)

