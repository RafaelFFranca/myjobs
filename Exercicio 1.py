#Exercício 1

def troca(vetor):
    for i in range(30):
        if vetor[i] >= 1:
            vetor[i] = 1
        else:
            vetor[i] = 0
    return vetor

vet = [0]*30
for i in range (30):
    vet[i] = int(input("digite um valor: "))
    
print (vet)

troca(vet)

print (vet)
