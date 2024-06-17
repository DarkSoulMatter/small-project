import random


print("NUMBER_GUESSING_GAME")
print("WELCOME\n")

life = 6
computer = random.randint(1, 100)
print("The random_number has chosen number from 1 to 100")


def guessing(number_life, random_number):
    print(f"you have {number_life} lives, Good Luck!!")
    while number_life > 0:
        user = input("\nguess the number\n-->\t")
        if check_user(user):
            user = int(user)
            if user < random_number:
                print("Your gues is too low!!")
                number_life -= 1
                print(f"Life remaining {number_life}")
            elif user > random_number:
                print("Your guess is too high!!")
                number_life -= 1
                print(f"Life remaining {number_life}")
            else:
                print("Your guess is correct!!")
                print(f"You won with {number_life} remaining lives")
                break
    if number_life == 0:
        print("\nYou have lost!!")
        print(f"The number was {random_number}")


def check_user(user):
    for char in user:
        if not char.isdigit():
            print("You entered a wrong value")
            return False
    return True


guessing(life, computer)
