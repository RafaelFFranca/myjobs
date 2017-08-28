#Exercício 2

def alteracao (lista):
    for i in range (5):
        if lista[i] < 0:
            lista[i] = 0
        elif lista[i] < 10:
            lista[i] = 1
        else:
            lista[i] = 2
    return lista

    
vet = [0]*5
for i in range (5):
    vet[i] = int(input (" Digite um número: "))

print (vet)

alteracao (vet)

print (vet)
