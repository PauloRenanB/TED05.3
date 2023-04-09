'''Faça um programa que receba um número e que calcule e mostre a tabuada desse número..
'''

valor = int(input('Digite um valor: '))
for i in range(1, 11):
    print(f'{valor}x{i}={valor*i}')