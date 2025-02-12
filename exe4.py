#Peça ao usuário para inserir sua cor favorita. Se ele digitar "vermelho", "VERMELHO" ou "Vermelho" exibem a mensagem "Eu também gosto de vermelho", caso contrário, exibem a mensagem "Eu não gosto de [cor], eu prefiro vermelho".
cor = input("qual é a sua cor favorita?")
if cor in ["vermelho","VERMELHO","Vermelho"]:
    print("eu também gosto de vermelho")
else:
    print("eu não gosto dessa cor, eu prefiro vermelho")
    print("joão henrique")