#Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$ 0,45 para viagens mais longas.
distancia = int(input("digite a distancia que deseja percorrer(km):"))
if distancia <= 200:
    passagem = distancia * 0.50
    print("a passagem fica por:", passagem,"reais.0,50" )
else:
    if distancia >200:
        passagem = distancia * 0.45
    print("a passagem fica por:", passagem,"reais.0,45" )
    print("joão henrique")