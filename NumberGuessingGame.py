import random
logo = '''

  _______  __    __   _______     _______.     _______.   .___________. __    __   _______    .__   __.  __    __  .___  ___. .______    _______ .______      
 /  _____||  |  |  | |   ____|   /       |    /       |   |           ||  |  |  | |   ____|   |  \ |  | |  |  |  | |   \/   | |   _  \  |   ____||   _  \     
|  |  __  |  |  |  | |  |__     |   (----`   |   (----`   `---|  |----`|  |__|  | |  |__      |   \|  | |  |  |  | |  \  /  | |  |_)  | |  |__   |  |_)  |    
|  | |_ | |  |  |  | |   __|     \   \        \   \           |  |     |   __   | |   __|     |  . `  | |  |  |  | |  |\/|  | |   _  <  |   __|  |      /     
|  |__| | |  `--'  | |  |____.----)   |   .----)   |          |  |     |  |  |  | |  |____    |  |\   | |  `--'  | |  |  |  | |  |_)  | |  |____ |  |\  \----.
 \______|  \______/  |_______|_______/    |_______/           |__|     |__|  |__| |_______|   |__| \__|  \______/  |__|  |__| |______/  |_______|| _| `._____|
                                                                                                                                                              
'''

print(logo)
print("Welcome to number guessing Game")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

number = random.randint(0,101)
def playGame():
    if difficulty == 'easy':
        attempts = 10
        print(f"You have {attempts} attempts reamianing to guess the number")
        guess = int(input("Make a guess: "))
        while attempts > 0:
            if guess > number:
                attempts -= 1
                print("Too High.")
                print("Guess again")
                print(f"You have {attempts} attempts reamianing to guess the number")
                guess = int(input("Make a guess: "))
            elif guess < number:
                attempts -= 1
                print("Too Low.")
                print("Guess again")
                print(f"You have {attempts} attempts reamianing to guess the number")
                guess = int(input("Make a guess: "))
            if guess == number: 
                print("You won!")
                break
            if attempts == 1:
                print("You lost")
                break

    elif difficulty == 'hard':
        attempts = 5
        print(f"You have {attempts} attempts reamianing to guess the number")
        guess = int(input("Make a guess: "))
        while attempts > 0:
            if guess > number:
                attempts -= 1
                print("Too High.")
                print("Guess again")
                print(f"You have {attempts} attempts reamianing to guess the number")
                guess = int(input("Make a guess: "))
            elif guess < number:
                attempts -= 1
                print("Too Low.")
                print("Guess again")
                print(f"You have {attempts} attempts reamianing to guess the number")
                guess = int(input("Make a guess: "))
            if guess == number: 
                print("You won!")
                break
            if attempts == 1:
                print("You lost")
                break

playGame()