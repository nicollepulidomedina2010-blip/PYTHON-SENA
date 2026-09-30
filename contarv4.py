palabra=input("Que palabra deseas mostrar")
print (f"la palabra que deseas es{palabra} ")

print ("indice   letra")
for indice,    letra in  enumerate (palabra):
    print(indice,"          ",letra)
