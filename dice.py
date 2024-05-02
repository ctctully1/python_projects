import random


def roll_dice(amount):
    #Rolls amount number of dice and return the results as a list.

    if amount <= 0:
        raise ValueError

    rolls = []
    for i in range(amount):
        random_roll = random.randint(1, 6)
        rolls.append(random_roll)

    return rolls


def main():
    while True:
        try:
            user_input = input('How many dice would you like to roll? Type exit to stop \n')

            # To exit the game
            if user_input.lower() == 'exit':
                print('Thanks for playing!')
                break

            # Try to parse the user_input to int
            print(*roll_dice(int(user_input)), sep=', ')
        except ValueError:
            print('(Please enter a valid number)')


if __name__ == '__main__':
    main()
