#variables
firstTerm = int(input("Primeiro termo: "))
reason = int(input("Digite a razão: "))
choiceUser = int(input("Mostrar quantos termos: "))
contador = 0
n = 1
#conditions
if choiceUser == 0:
  print("Até Logo...")
#loop
while contador < choiceUser:
  term = firstTerm + (n - 1) * reason# formule
  contador += 1
  n += 1
  print(term,end=" > ")
print("Fim")
