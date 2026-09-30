#Mi segunda funcion
#Aqui utulizo parametro o argumentos. Tambien utilizo return
#Developer: Nicolle Sofia Pulido

def saludar_persona(nombre):
    print(f"Hola {nombre.upper()}")

 #Llamamos la funcion
saludar_persona('sofia')


#PARTE 2. Utilizamos return 
def sumar(a,b):
    resultado= a + b # a y b son variables de ambito LOCAL
    return resultado 

#Llamamos la funcion sumar
total=sumar(3,5)

print (f"el total es {total}")
