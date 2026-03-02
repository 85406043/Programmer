"""Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o."""
#variables
listNumbersPairs = [] #list
sum = 0
#loop
for integer in range(1, 7):
  number = int(input("Enter a number: "))
  if number % 2 == 0:
    listNumbersPairs.append(number)
    sum += number
  else:
    pass
#Show result
print(f"Numbers Pairs: {listNumbersPairs}")
print(f"The sum between pairs: {sum}")
