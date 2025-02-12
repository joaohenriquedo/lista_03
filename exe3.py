#Peça ao usuário para inserir um número entre 10 e 20 (inclusive). Se ele inserir um número dentro desse intervalo, exiba a mensagem "Obrigado", caso contrário, exiba a mensagem "Resposta incorreta".
nun = int(input("digite um número entre 10 e 20: "))
if 10 <= nun <= 20:
    print("obrigado")
else:
    print("resposta incorreta")
print("joão henrique")