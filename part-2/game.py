import random

while True:
    choices = ['rock', 'paper', 'scissors']

    computer = random.choice(choices)

    player = None

    player_points = 0
    computer_points = 0

    while player not in choices:
        player = input("rock, paper or scissors? ").lower()

    if player == computer:
        print("Computer: ", computer)
        print("Player: ", player)
        print("It's a tie!")

    elif player == 'rock':
        if computer == 'paper':
            print("Computer: ", computer)
            print("Player: ", player)
            print("You lose!")
            computer_points += 1

        if computer == 'scissors':
            print("Computer: ", computer)
            print("Player: ", player)
            print("You win!")
            player_points += 1
        
    elif player == 'paper':
        if computer == 'scissors':
            print("Computer: ", computer)
            print("Player: ", player)
            print("You lose!")
            computer_points += 1

        if computer == 'rock':
            print("Computer: ", computer)
            print("Player: ", player)
            print("You win!")
            player_points += 1

    elif player == 'scissors':
        if computer == 'rock':
            print("Computer: ", computer)
            print("Player: ", player)
            print("You lose!")
            computer_points += 1

        if computer == 'paper':
            print("Computer: ", computer)
            print("Player: ", player)
            print("You win!")
            player_points += 1

    print("You: ", player_points)
    print("Computer: ", computer_points)

    play_again = input("Do you want to play again? (yes/no) ").lower()

    if play_again != 'yes':
        break
