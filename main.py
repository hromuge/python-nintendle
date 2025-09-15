import csv, random

path = "./nintendo_characters.csv"
characters = []
guesses = 5
guessed_letters = []

with open(path, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        characters.append(row[0])
    f.close()

current_character = random.choice(characters)

def check_guess(entered_guess):
    if entered_guess == current_character:
        return True
    else:
        for char in entered_guess:
            if list(current_character).__contains__(char):
                guessed_letters.append(char)
        return False

def create_censored_guess():
    output = ''
    for char in current_character:
        if not char == ' ':
            if char in guessed_letters:
                output += char
            else:
                output += '_'
        else:
            output += ' '
    return output

print('\nWelcome to Nintendle. Like wordle, but with your favorite Nintendo characters! \nEnter your guess and hit "Enter" to try your luck!\n')
while guesses > 0:
    guess = input(f'Your Character is: {create_censored_guess()}. \nYou have {guesses} guesses left. \nType here to guess: ')
    if check_guess(guess):
        print(f'You guessed the character correctly! It was: {current_character}!')
        guesses = 0
        exit(0)
    else:
        print('Incorrect. Try again!')
        guesses -= 1

print(f'\nYou have no guesses remaining. \nThe Character was {current_character}. Thank you for playing!')
exit(0)
