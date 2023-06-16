import random

word_list = ["aardvark", "baboon", "camel"]


def main():
    chosen_word = random.choice(word_list)
    display_word = ""
    total_strikes = 6
    strikes = 0
    guesses = []
    guesses.clear()
    for letter in chosen_word:
        display_word += "_"
    check_guess(chosen_word, display_word, strikes, total_strikes, guesses)


def check_guess(chosen_word, display_word, strikes, total_strikes, guesses):
    if display_word == chosen_word:
        print(f"The word was {chosen_word}! You got it right!")
        print(
            f"You had {strikes} wrong guesses, out of a total of {total_strikes} ."
        )
        print("You won!")
        replay()
    elif strikes >= total_strikes:
        print("You lost!")
        replay()
    else:
        check_again(chosen_word, display_word, strikes, total_strikes, guesses)
              
def check_again(chosen_word, display_word, strikes, total_strikes,
                            guesses):
    valid_guess = validate_guess(chosen_word, display_word, strikes, total_strikes, guesses)
    position = 0
    correct = 0
    if valid_guess:
      for letter in chosen_word:
        position += 1
        if letter == valid_guess:
          print(f"The letter: {valid_guess} is found in the word at position: {position}.")
          display_word = display_word[:position -1] + letter + display_word[ position:]
          correct = 1

      if correct == 1:
        check_guess(chosen_word, display_word, strikes, total_strikes,guesses)

      else:
        strikes += 1
        print( f"The letter: {valid_guess} you chose is wrong. That is a strike, you have {strikes} out of {total_strikes}.")
        check_guess(chosen_word, display_word, strikes, total_strikes, guesses)


def validate_guess(chosen_word, display_word, strikes, total_strikes, guesses):
    print(f"Your current word is: {display_word}.")
    print(f"Your current guesses are: {guesses} \n")
    guess = input("Please type in the letter for your guess. Your guess: \n").lower()
    redo = 0
    for item in guesses:
        if guess == item:
            redo = 1
            print(
                "You have already selected this letter, please try again. \n")
    if redo == 1:
        check_again(chosen_word, display_word, strikes, total_strikes, guesses)
    else:
        guesses += guess
        return guess


def replay():
    retry = input(
        "Would you like to play again? Type Y or N. Your choice: ").lower()
    if retry == "y":

        main()


main()
