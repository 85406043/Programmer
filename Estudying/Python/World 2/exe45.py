#import modules
import random
import time
#choise user
print("Game Jokenpô")
print("==-"*50)
userChoise = int(input("""Choose between:
      [1] Rock
      [2] Paper
      [3] Scissors
      => """))

#CPU
listCpu = ["Rock", "Paper", "Scissors"]
choiseCPU = random.choice(listCpu)

time.sleep(0.5)
print("JO")
time.sleep(1)
print("KEN")
time.sleep(1)
print("PO!!!")

#conditions

