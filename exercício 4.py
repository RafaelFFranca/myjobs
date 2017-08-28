arquivo = open ("novo_arquivo.txt" , "w")
for i in range (1):
    arquivo.write ("Estou cursando Banco de Dados!")
arquivo.close()

arquivo = open ("novo_arquivo.txt" , "r")
for linha in arquivo:
    print ("" , linha)
arquivo.close()

arquivo = open ("arquivo.txt" , "r")
copia_arq = open ("copia_arq.txt" , "w")
while 1:
    texto = arquivo.read(35)
    if texto == "":
        break
    copia_arq.write(texto)
arquivo.close()
copia_arq.close()
