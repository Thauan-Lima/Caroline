"""4. Implementar um programa que leia um valor inteiro via teclado, em seguida
verifique se o número é posiLvo, negaLvo ou zero. Como saída, exiba na tela a
mensagem “O número é posiLvo”, “O número é negaLvo” ou “o número é zero”."""
n = int(input("Número inteiro: "))
if n > 0:
    print("O número é positivo.")
elif n == 0:
    print("O número é zero.")
elif n < 0:
    print("O número é negativo.")
else:
    print("Valor inválido.")