import random
while True:
    player1 = input("enter [r/p/s]  : ")
    choices = ["r","p","s"]
    comp = random.choice(choices)
    print(comp)
    print(player1)
    break
