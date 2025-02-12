#Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.
salario = int(input("insira o seu salario:"))
if salario >1250:
    aumento = salario * 0.10
    print("o aumento salarial foi de:", aumento, "reais. 15%")
else:
    aumento = salario * 0.15
    print("o aumento salarial foi de:", aumento, "reais. 10%")
    print("joão henrique")