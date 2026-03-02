"""Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o."""

listNumbersPairs = []
listNumbersOdd = []

for integer in range(1, 7):
  number = int(input("Enter a number: "))
  if number % 2 == 0:
    listNumbersPairs.append(number)
  else:
    pass

print(f"Numbers Pairs: {", ".join(listNumbersPairs)}.")
