espaco = open ("espaco.txt" , "w")
for i in range (1):
    espaco.write('''ACME Inc. Uso do espaço em disco pelos usuários
-----------------------------------------------------------------------
Nr. Usuário Espaço utilizado % do uso
1 alexandre 434,99 MB 16,85%
2 anderson 1187,99 MB 46,02%
3 antonio 117,73 MB 4,56%
4 carlos 87,03 MB 3,37%
5 cesar 0,94 MB 0,04%
6 rosemary 752,88 MB 29,16%
Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB''')
espaco.close()
espaco = open ("espaco.txt" , "r")
for i in espaco:
    print (i)
espaco.close()

