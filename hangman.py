# Step 1: Word Selection
import random

# Words dictionary with hints
words = {"Lion": "Mammal", "Eagle": "Bird", "Snake": "Reptile"}
word, hint = random.choice(list(words.items()))
word = word.lower()

# Initialize blanks as a list of underscores
blanks = ["_"] * len(word)

# Step 2: Display Hangman and Blanks
def display_hangman(attempts):
    stages = [
        "",
        " O ",
        " O\n | ",
        " O\n/| ",
        " O\n/|\\",
        " O\n/|\\\n/ ",
        " O\n/|\\\n/ \\"
    ]
    print(stages[attempts])

def display_blanks():
    print(" ".join(blanks))

# Step 3: Game Loop
attempts = 0
max_attempts = 6
guessed = []

while attempts < max_attempts and "_" in blanks:
    display_hangman(attempts)
    display_blanks()
    print(f"Hint: {hint}")
    
    guess = input("Guess a letter: ").lower()
    
    if guess in guessed:
        print("Already guessed! Try again.")
    elif guess in word:
        # Update blanks with correctly guessed letters
        for i, letter in enumerate(word):
            if letter == guess:
                blanks[i] = guess
        guessed.append(guess)  # Track guessed letters
    else:
        attempts += 1
        guessed.append(guess)
        print(f"Wrong guess '{guess}'")

# Step 4: End Game
if "_" not in blanks:
    print("You win! The word was:", word)
else:
    display_hangman(attempts)
    print("You lose! The word was:", word)
