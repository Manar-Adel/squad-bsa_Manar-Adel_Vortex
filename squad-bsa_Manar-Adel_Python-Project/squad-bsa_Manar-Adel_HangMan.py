#Hang Man Game

#all team members
word = "python"
chances = 8
guesses = []
done = False

while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("")

    guess = input(str(chances) + " chances left, enter a letter: ")
    guesses.append(guess.lower())
    if guess.lower() not in word.lower():
        chances -=1
        if chances == 0:
            break

    done = True
    for letter in word:
        if letter.lower() not in guesses:
            done = False

if done:
    print("you win! the word is Python")
else:
    print("game over! the word was Python")





