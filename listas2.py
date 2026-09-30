#Filtrar lementos de una lista 
def obtener_pares(lista_numeros):
    pares = [] # Listas vacias
    #ciclo para buscar los pares
    for num in lista_numeros:
        if num % 2 == 0: #Pregunto siel numero es PAR 
            pares.append(num)#Añadios el numero a la lista nueva
    return pares

    #------------------------
        
lista_numeros = [8,7,4,2988,9500]
print(obtener_pares(lista_numeros))
       

