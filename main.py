import random
while True:
    player = input("enter [rock/paper/scissors]  : ")
    choices = ["rock","paper","scissors"]
    comp = random.choice(choices)
    print(f"player has entered {player}")
    print(f"computer has entered {comp}")
    if player == comp:
        print("tie")
    if player == "rock" and comp == "paper":
        print("The computer won. Paper beats rock")
    if comp == "rock" and player == "paper":
        print("The player won. Paper beats rock")
    if player == "rock" and comp == "scissors":
        print("The player won. Rock beats scissors")
    if comp == "rock" and player == "scissors":
        print("The computer won. Rock beats scissors")
    if player == "paper" and comp == "scissors":
        print("The computer won. Scissors beats paper")
    if comp == "paper" and player == "scissors":
        print("The player won. Scissors beats paper")

    x = input("would you like to play again y/n ? : ")
    if x.lower() == "n":
        break
    else:
        pass

