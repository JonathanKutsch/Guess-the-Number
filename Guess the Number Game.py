import random


while True:
    number = random.randint(1, 10)
    tries = 0
    win = False

    name = input("Hello, what is your username?" )

    print("Hello " + name + ".")

    question = input("Would you like to play a game? [Y/N] ")
    if question.lower() == "n":
        print("Fine... be like that.")

    if question.lower() == "no":
        print("Fine... be like that.")
        exit()

    if question.lower() == "y":
        print("I'm thinking of a number between 1 & 10")
    if question.lower() == "yes":
        print("I'm thinking of a number between 1 & 10")
    while not win:
        guess = int(input("Guess the number: "))
        tries = tries + 1
        if guess == number:
            win = True
        elif guess < number:
            print("Guess Higher")
        elif guess > number:
            print("Guess Lower")

    print("Congrats, you guessed correctly. The number was indeed {}".format(number))
    print("It took you {} tries.".format(tries))

    answer = input("Restart? [Y/N]")
    if answer == "no" or answer == "N" or answer == "No" or answer == "n":
        print("Leaving the Game.")
        exit()
    elif answer == "yes" or answer == "Y" or answer == "yes" or answer == "y":
        print("Starting new game.")