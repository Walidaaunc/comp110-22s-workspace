"""EX02 - One Shot Wordle!"""

__author__ = "730507751"

secret_word: str = "python"
users_word: str = input("What is your 6-letter guess? ")

while len(users_word) != len(secret_word):
    users_word = input("That was not 6 letters! Try again: ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
i: int = 0
screen_display: str = ""
while i < len(secret_word):
    if users_word[i] == secret_word[i]:
        screen_display = screen_display + GREEN_BOX
    else:
        t_or_f_variable: bool = False
        alternate_i: int = 0
        while t_or_f_variable is not True and alternate_i < len(secret_word):
            t_or_f_variable = users_word[i] == secret_word[alternate_i]
            alternate_i = alternate_i + 1
        if t_or_f_variable is True:
            screen_display = screen_display + YELLOW_BOX
        else:
            screen_display = screen_display + WHITE_BOX
    i = i + 1

print(screen_display)
if users_word != secret_word:
    print("Not quite. Play again soon!")
else:
    print("Woo! You got it!")