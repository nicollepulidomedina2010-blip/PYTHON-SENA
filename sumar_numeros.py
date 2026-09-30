#Funciones con ciclos
def sumar_lista(numeros):
    total = 0
    for num in numeros:
        #total=total + num
        total+= num
    return total

#----------------------

numeros=[30,20,10]
print (sumar_lista(numeros))
