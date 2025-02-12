#Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h.
velocidade = int(input("qual é a velocidade do seu carro (em km/h)? "))
if velocidade > 80:
    multa = (velocidade - 80) * 5
    print("voce foi multado, o valor da multa é:", multa ,"reais")
else:
    print("voce está dentro do limite de velocidade. Tenha um bom dia!")
    print("joão henrique")
