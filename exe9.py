#Escreva um programa que faça o cálculo do imposto de renda 2025. Consulte a tabela no site da Receita federal.
renda = int (input("digite sua renda anual: R$ "))
imposto = 0
if renda <= 22847.76:
    imposto = 0
elif renda <= 33919.80:
    imposto = (renda - 22847.76) * 0.075
elif renda <= 45012.60:
    imposto = (renda - 33919.80) * 0.15 + 826.15
elif renda <= 55976.16:
    imposto = (renda - 45012.60) * 0.225 + 1427.57
else:
    imposto = (renda - 55976.16) * 0.275 + 2117.02
if imposto > 0:
    print("voce deve pagar: de Imposto de Renda.")
else:
    print("voce está isento de pagar Imposto de Renda.")
    print("joão henrique")
