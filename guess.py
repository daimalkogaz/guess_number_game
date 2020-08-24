from random import randint
guess_left = 25


def generator():
    return randint(1, 10)


def rand_guess():
    global guess_left
    random_number = generator()

    flag = 0

    while guess_left > 0:
        guess = int(input("Please enter your lucky number: "))
        if guess == random_number:
            flag = 1
            break
        elif guess < random_number:
            guess_left -= 1
            print(f"Wrong Guess. Your number should be higher! You have {guess_left} tries left.")
        else:
            guess_left -= 1
            print(f"Wrong Guess. Your number should be lower! You have {guess_left} tries left.")

    if flag == 1:
        return True
    else:
        return False


if __name__ == '__main__':
    if rand_guess() is True:
        print(f"Congrats! You won after {26 - guess_left} tries.")
    else:
        print("Sorry, you lost the game!")
