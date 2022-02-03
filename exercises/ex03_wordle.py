"""EX03 - Wordle with functions!"""

__author__ = "730507751"


def contains_char(given_string: str, given_single_character: str) -> bool:
    """Returns True if the single character of the second string is found at any index of the first string, and returns False otherwise."""
    assert len(given_single_character) == 1
    index: int = 0
    true_or_false: bool = False

    while index < len(given_string) and true_or_false is not True:
        if given_single_character == given_string[index]:
            true_or_false = True
        index += 1
    return true_or_false


def emojified(guessed_string: str, the_secret_string: str) -> str:
    """Returns string of emoji whose color codifies green, yellow or white boxes."""
    assert len(guessed_string) == len(the_secret_string)
    i: int = 0
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    display_screen: str = ""
    while i < len(the_secret_string):
        if guessed_string[i] == the_secret_string[i]:
            display_screen = display_screen + GREEN_BOX
        elif contains_char(the_secret_string, guessed_string[i]) is True:
            display_screen = display_screen + YELLOW_BOX
        else:
            display_screen = display_screen + WHITE_BOX
        i = i + 1
    return display_screen


def input_guess(expected_length: int) -> str:
    """Prompts the user for a guess, then returns the users guess of the correct length to the caller."""
    stored_value: int = expected_length
    given_string: str = input("Enter a " + str(stored_value) + " character word: ")
    while len(given_string) != stored_value:
        given_string: str = input("That wasn't " + str(stored_value) + " chars! Try again: ")
    return given_string


def main() -> None:
    """The entrypoint of the program and main game loop."""
    the_secret_word: str = "codes"
    turns_played_by_user: int = 1
    the_user_won: bool = False
    users_input: str = ""
    while turns_played_by_user < 7 and the_user_won is not True:
        print("=== Turn " + str(turns_played_by_user) + "/6 ===")
        users_input = input_guess(5)
        print(emojified(users_input, the_secret_word))
        if users_input == the_secret_word:
            the_user_won = True
            print("You won in " + str(turns_played_by_user) + "/6 turns!")
        turns_played_by_user += 1
    if the_user_won is not True:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()