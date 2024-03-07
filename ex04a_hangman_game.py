import random
import string

class Hangman:
    def __init__(self):
        self.words = ["apple", "banana", "cherry", "date", "elderberry"]
        self.word_to_guess = random.choice(self.words)
        self.guessed_letters = set()
        self.max_attempts = 6

    def greet_user(self):
        print("Welcome to Hangman!")

    def display_word(self):
        display = ""
        for letter in self.word_to_guess:
            if letter in self.guessed_letters:
                display += letter
            else:
                display += "_"
        print(display)

    def play(self):
        self.greet_user()

        while True:
            self.display_word()
            guess = input("Guess a letter: ").lower()

            if len(guess) != 1 or guess not in string.ascii_lowercase:
                print("Please enter a single letter.")
                continue

            self.guessed_letters.add(guess)

            if guess not in self.word_to_guess:
                self.max_attempts -= 1
                print(f"Wrong guess! {self.max_attempts} attempts left.")

            if self.max_attempts == 0:
                print(f"Game over! The word was '{self.word_to_guess}'.")
                break

            if all(letter in self.guessed_letters for letter in self.word_to_guess):
                print(f"Congratulations! You guessed the word: '{self.word_to_guess}'.")
                break

if __name__ == "__main__":
    game = Hangman()
    game.play()
