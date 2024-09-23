import random
from hangman_art import hm_art, stages
from hangman_words import word_list

print(hm_art)

placeholder = ""
lives = 6

chosen_word = random.choice(word_list)

for word in chosen_word:
    placeholder = placeholder + "_"

print(placeholder)
game_over = False
correct_letters = []

while not game_over:
    print(f"********* You've got {lives} lives left *********")
    guess = input("Guess a letter: ").lower()

    display = ""
    for letter in chosen_word:
        if letter == guess:
            display = display + letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display = display + letter
        else:
            display = display + "_"

    if guess not in chosen_word:
        lives = lives - 1
        print(f"You've guessed {guess}, that's not the word. You lose a life. ")

        if lives == 0:
            game_over = True
            print(f"************* IT WAS {chosen_word}! YOU LOSE *************")
    print(display)

    if "_" not in display:
        game_over = True
        print("************* YOU WIN *************")

    print(stages[lives])