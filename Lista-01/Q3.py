"""3. Implementar um programa que leia dois valores inteiros via teclado, em
seguida, calcule a divisão entre eles, e como saída, exiba na tela o dividendo,
o divisor, o quociente e o resto."""
a = int(input("Primeiro valor inteiro: "))
b = int(input("Segundo valor inteiro: "))
q = a/b
r = a%b
print("Dividendo: ", a)
print("Divisor: ", b)
print("Quociente: ", q)
print("Resto: ", r)