import random
words = ["apple", "banana", "python", "orange", "computer"]
word = random.choice(words)
guessed = []
attempts = 6
print("welcome to Hangman Game!")
while attempts > 0:
    display = " "
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += " "
            print(display)
            if "-" not in display:
             print("you won!")
            break
            guess = input("Enter a letter:").lower()
            if guess in word:
                guessed.append(guess)
                print("Correct!")
            else:
                attempts -=1
                print("Wrong! Attempts left:", attempts)
                if attempts == 0:
                    print("Game Over!")
                    print("The word was:", word)
