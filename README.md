import random


######################################################
print("NUMBER_GUESSING_GAME")
print("WELCOME\n")

lives = 6

computer = random.randint(1, 100)
print("The computer has chosen number from 1 to 100")


def guessing(lives, computer):
    print(f"you have {lives} lives, Good Luck!!")
    while lives > 0 :
        user = int(input("\nguess the number\n-->\t"))
        if user < computer:
            print("Your gues is too low!!")
            lives -= 1
            print(f"Life remaining {lives}")
        elif user > computer:
            print("Your guess is too high!!")
            lives -= 1
            print(f"Life remaining {lives}")
        else:
            print("Your guess is corret!!")
            print(f"You won with {lives} remaining lives")
            break

    if lives == 0:
        print("\nYou have lost!!")
        print(f"The number was {computer}")

guessing(lives, computer)
#################################################################

