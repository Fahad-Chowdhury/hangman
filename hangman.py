import random

from words_list import words
from ascii_art import hangman_word_art, lives_art

words = words.splitlines()
choosen_word = random.choice(words).lower()
word_list = ['_'] * len(choosen_word)
guessed_letters = []
lives = 6
game_over = False

print(hangman_word_art)

while not game_over:
    if guessed_letters:
        guessed_str = ', '.join(guessed_letters)
        print(f"\nGuess again . . .\n")
        print(f"Letters you have guessed previously: {guessed_str}")
    word_to_guess = ''.join(word_list)
    print(f"\nWord to guess: {word_to_guess}")
    guessed_letter = input("\nGuess a letter: ").lower()
    if guessed_letter in guessed_letters:
        print(f"You already guessed {guessed_letter} before, try again.")
    elif guessed_letter in choosen_word:
        print(f"Correct Guess!")
        guessed_letters.append(guessed_letter)
        for index, ch in enumerate(choosen_word):
            if ch == guessed_letter:
                word_list[index] = ch
        print(''.join(word_list))
        if '_' not in word_list:
            print(f"\n\nYOU WIN! \\(ᵔᵕᵔ)/ \n")
            game_over = True
    else:
        lives -= 1
        guessed_letters.append(guessed_letter)
        print(f"You guessed {guessed_letter}, that's not in the word. You lose a life.")
        print(lives_art[lives])
        print(f"****************************{lives}/6 LIVES LEFT****************************")
        if lives <= 0:
            print(f"\n\nIT WAS {choosen_word}! YOU LOSE  (ᵟຶ︵ ᵟຶ) \n")
            game_over = True
